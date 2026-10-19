const fs = require('fs');
const path = require('path');
const { capture } = require('../core/capture');

const RENDERS_DIR = path.resolve(
    __dirname,
    '../../../content/software/app-lab/assets/renders'
);

// Measure the 5-column JCTL header pin pitch on each source render so both
// boards are displayed with an identically sized JCTL header:
// - UNO Q (1920x1080): 4 * 39px = 156px across columns 1..5
// - VENTUNO Q (3840x2160): 4 * 42px = 168px across columns 1..5
const UNO_Q_JCTL_PITCH = 39;
const VENTUNO_Q_JCTL_PITCH = 42;
const VENTUNO_Q_SCALE = UNO_Q_JCTL_PITCH / VENTUNO_Q_JCTL_PITCH;

const BOARDS = [
    {
        id: 'uno-q',
        output: 'flashing/uno-q-jctl-pins.png',
        renderFile: 'UNO Q_Top 01- 1080P.png',
        scale: 1,
        // Include margin around the top, left (USB-C), and right edges of the UNO Q PCB,
        // cropping below the ARDUINO / UNO Q logo.
        crop: { x: 400, y: 100, width: 1140, height: 560 },
        pinDiameter: 28,
        pins: [
            {
                // JCTL upper-right pin (Pin 2: GND)
                x: 812,
                y: 246,
                label: 'GND',
                labelSide: 'right',
                connectorSide: 'right',
                fixedX: 520,
                fixedY: 88,
                connectorMidX: 472
            },
            {
                // JCTL lower-right pin (Pin 1: USB_BOOT)
                x: 812,
                y: 287,
                label: 'USB_BOOT',
                labelSide: 'right',
                connectorSide: 'right',
                fixedX: 520,
                fixedY: 184,
                connectorMidX: 472
            }
        ]
    },
    {
        id: 'ventuno-q',
        output: 'flashing/ventuno-q-jctl-pins.png',
        renderFile: 'Ventuno_Q_Top_Without_Fan_4K.png',
        scale: VENTUNO_Q_SCALE,
        // Include margin outside the top-left corner of the VENTUNO Q PCB
        // (board top-left is at x=654, y=250 in 4K source coordinates)
        // and crop bottom/right at the matched JCTL scale.
        crop: {
            x: 590,
            y: 195,
            width: Math.round(1140 / VENTUNO_Q_SCALE),
            height: Math.round(560 / VENTUNO_Q_SCALE)
        },
        pinDiameter: 28,
        pins: [
            {
                // JCTL upper-right pin (Pin 1: GND)
                x: 1068,
                y: 493,
                label: 'GND',
                labelSide: 'right',
                connectorSide: 'right',
                fixedX: 555,
                fixedY: 204,
                connectorMidX: 518
            },
            {
                // JCTL lower-right pin (Pin 2: FORCE_BOOT)
                x: 1068,
                y: 534,
                label: 'FORCE_BOOT',
                labelSide: 'right',
                connectorSide: 'right',
                fixedX: 555,
                fixedY: 300,
                connectorMidX: 518
            }
        ]
    }
];

async function renderBoardScene(page, board) {
    const imgBuffer = fs.readFileSync(path.join(RENDERS_DIR, board.renderFile));
    const imgUrl = `data:image/png;base64,${imgBuffer.toString('base64')}`;
    const width = Math.round(board.crop.width * board.scale);
    const height = Math.round(board.crop.height * board.scale);

    await page.setViewportSize({ width, height });

    const pinElementsHtml = board.pins
        .map((pin, idx) => {
            const cx = (pin.x - board.crop.x) * board.scale;
            const cy = (pin.y - board.crop.y) * board.scale;
            const r = board.pinDiameter / 2;
            return `<div id="pin-${idx}" style="position:fixed; left:${cx - r}px; top:${cy - r}px; width:${board.pinDiameter}px; height:${board.pinDiameter}px; border-radius:50%;"></div>`;
        })
        .join('\n');

    const html = `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  html, body {
    margin: 0;
    padding: 0;
    width: ${width}px;
    height: ${height}px;
    overflow: hidden;
    background: #ffffff;
  }
  #scene {
    position: relative;
    width: ${width}px;
    height: ${height}px;
    overflow: hidden;
    background: #ffffff;
  }
  #board-img {
    position: absolute;
    left: ${-board.crop.x * board.scale}px;
    top: ${-board.crop.y * board.scale}px;
    transform: scale(${board.scale});
    transform-origin: top left;
    display: block;
    user-select: none;
    pointer-events: none;
  }
</style>
</head>
<body>
  <div id="scene">
    <img id="board-img" src="${imgUrl}" />
    ${pinElementsHtml}
  </div>
</body>
</html>`;

    await page.setContent(html, { waitUntil: 'load' });
    await page.evaluate(() => {
        const img = document.getElementById('board-img');
        if (img && !img.complete) {
            return new Promise((resolve, reject) => {
                img.onload = resolve;
                img.onerror = reject;
            });
        }
    });
}

async function runRendersFlow(page, outDir, options = {}) {
    const { step = 'all' } = options;

    for (const board of BOARDS) {
        if (step !== 'all' && step !== 'flashing' && step !== board.id) {
            continue;
        }
        console.log(`\n--- Rendering ${board.id} JCTL pins ---`);
        await renderBoardScene(page, board);

        const scene = page.locator('#scene');
        const highlights = board.pins.map((pin, idx) => ({
            locators: page.locator(`#pin-${idx}`),
            label: pin.label,
            labelSide: pin.labelSide,
            connectorSide: pin.connectorSide,
            fixedX: pin.fixedX,
            fixedY: pin.fixedY,
            connectorMidX: pin.connectorMidX,
            shape: 'circle',
            fill: 'rgba(255, 140, 0, 0.25)',
            outlineWidth: 6,
            strokeWidth: 4,
            fontSize: 28,
            badgePadding: '8px 20px',
            badgeRadius: 6
        }));

        await capture(page, board.output, outDir, {
            highlight: highlights,
            crop: scene,
            omitBackground: false
        });
    }
}

runRendersFlow.skipBaseUrl = true;
module.exports = runRendersFlow;
