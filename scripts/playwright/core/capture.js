const fs = require('fs');
const path = require('path');

const CONFIG = {
    baseUrl: 'http://localhost:34115',
    viewport: { width: 1282, height: 720 }
};

async function highlightElement(page, highlightDefs, isInsetGlobal = false) {
    const defsWithHandles = [];
    for (const def of highlightDefs) {
        const locs = Array.isArray(def.locators) ? def.locators : [def.locators];
        const handles = [];
        for (const loc of locs) {
            const handle = await loc.elementHandle();
            if (handle) handles.push(handle);
        }
        if (handles.length > 0) {
            defsWithHandles.push({ 
                nodes: handles, 
                label: def.label, 
                side: def.labelSide || 'top',
                connectorSide: def.connectorSide || null,
                inset: def.inset !== undefined ? def.inset : isInsetGlobal,
                alignVertical: def.alignVertical || false,
                fixedY: def.fixedY !== undefined ? def.fixedY : null,
                connectorMidX: def.connectorMidX !== undefined ? def.connectorMidX : null
            });
        }
    }

    if (defsWithHandles.length === 0) return [];

    return await page.evaluate((defs) => {
        const labelRectsResult = [];
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('class', 'playwright-highlight-overlay');
        svg.style.cssText = 'position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:999997;';
        document.body.appendChild(svg);

        const highlightBoxes = defs.map(def => {
            const rects = def.nodes.map(n => n.getBoundingClientRect());
            return {
                top: Math.min(...rects.map(r => r.top)),
                left: Math.min(...rects.map(r => r.left)),
                bottom: Math.max(...rects.map(r => r.bottom)),
                right: Math.max(...rects.map(r => r.right))
            };
        });

        const items = [];
        const gap = 30; 
        const margin = 15; 
        const labelMargin = 20; 

        defs.forEach((def, i) => {
            const box = highlightBoxes[i];
            const bw = box.right - box.left;
            const bh = box.bottom - box.top;
            const boxCx = box.left + bw / 2;
            const boxCy = box.top + bh / 2;

            console.log(`[Box] Def ${i} (${def.label || 'no-label'}): left=${box.left}, right=${box.right}, top=${box.top}, bottom=${box.bottom}, cx=${boxCx}, cy=${boxCy}`);

            const overlay = document.createElement('div');
            overlay.className = 'playwright-highlight-overlay';
            overlay.style.cssText = `
                position: fixed; pointer-events: none; z-index: 999998;
                top: ${box.top}px; left: ${box.left}px; width: ${bw}px; height: ${bh}px;
                outline: 4px solid #FF8C00; outline-offset: ${def.inset ? '-4px' : '2px'};
                border-radius: 4px;
            `;
            document.body.appendChild(overlay);

            if (def.label) {
                const badge = document.createElement('div');
                badge.innerText = def.label;
                badge.className = 'playwright-highlight-overlay';
                badge.style.cssText = `
                    position: fixed; z-index: 999999; background-color: #FF8C00; color: white;
                    padding: 4px 12px; font-size: 14px; font-weight: bold; font-family: sans-serif;
                    border-radius: 4px; white-space: nowrap; visibility: hidden; top: 0; left: 0;
                `;
                document.body.appendChild(badge);
                const br = badge.getBoundingClientRect();
                
                items.push({
                    def, box, badge, boxCx, boxCy,
                    w: br.width, h: br.height, 
                    side: def.side,
                    cx: boxCx, 
                    cy: boxCy,
                    alignVertical: def.alignVertical || false,
                    fixedY: def.fixedY !== undefined ? def.fixedY : null,
                    connectorMidX: def.connectorMidX !== undefined ? def.connectorMidX : null
                });
            }
        });

        const sides = { 'top': [], 'bottom': [], 'left': [], 'right': [] };
        items.forEach(item => sides[item.side].push(item));

        ['top', 'bottom'].forEach(side => {
            const group = sides[side];
            if (group.length === 0) return;
            group.sort((a, b) => a.boxCx - b.boxCx); 
            for (let iter = 0; iter < 100; iter++) {
                group.forEach(item => { item.cx += (item.boxCx - item.cx) * 0.1; });
                for (let i = 0; i < group.length - 1; i++) {
                    let a = group[i], b = group[i+1];
                    let minDist = (a.w + b.w) / 2 + labelMargin;
                    if (b.cx - a.cx < minDist) { b.cx = a.cx + minDist; }
                }
                let last = group[group.length - 1];
                let rLimit = window.innerWidth - margin - last.w/2;
                if (last.cx > rLimit) last.cx = rLimit;
                for (let i = group.length - 1; i > 0; i--) {
                    let b = group[i], a = group[i-1];
                    let minDist = (a.w + b.w) / 2 + labelMargin;
                    if (b.cx - a.cx < minDist) { a.cx = b.cx - minDist; }
                }
                let first = group[0];
                let lLimit = margin + first.w/2;
                if (first.cx < lLimit) first.cx = lLimit;
            }
            group.forEach(item => {
                item.finalY = side === 'top' ? item.box.top - item.h - gap : item.box.bottom + gap;
                item.finalX = item.cx - item.w / 2;
            });
        });

        ['left', 'right'].forEach(side => {
            const group = sides[side];
            if (group.length === 0) return;
            group.sort((a, b) => {
                if (Math.abs(a.boxCy - b.boxCy) > 8) {
                    return a.boxCy - b.boxCy;
                }
                return a.boxCx - b.boxCx;
            });
            const colX = side === 'left' 
                ? Math.min(...group.map(g => g.box.left)) - gap
                : Math.max(...group.map(g => g.box.right)) + gap;

            for (let iter = 0; iter < 100; iter++) {
                group.forEach(item => {
                    if (item.alignVertical) {
                        item.cy = item.boxCy;
                    } else if (item.fixedY !== null) {
                        item.cy = item.fixedY + item.h / 2;
                    } else {
                        item.cy += (item.boxCy - item.cy) * 0.1;
                    }
                });
                for (let i = 0; i < group.length - 1; i++) {
                    let a = group[i], b = group[i+1];
                    if (b.alignVertical || b.fixedY !== null) continue;
                    let minDist = (a.h + b.h) / 2 + labelMargin;
                    if (b.cy - a.cy < minDist) { b.cy = a.cy + minDist; }
                }
                let last = group[group.length - 1];
                let bLimit = window.innerHeight - margin - last.h/2;
                if (last.cy > bLimit && !last.alignVertical && last.fixedY === null) last.cy = bLimit;
                for (let i = group.length - 1; i > 0; i--) {
                    let b = group[i], a = group[i-1];
                    if (a.alignVertical || a.fixedY !== null) continue;
                    let minDist = (a.h + b.h) / 2 + labelMargin;
                    if (b.cy - a.cy < minDist) { a.cy = b.cy - minDist; }
                }
                let first = group[0];
                let tLimit = margin + first.h/2;
                if (first.cy < tLimit && !first.alignVertical && first.fixedY === null) first.cy = tLimit;
            }
            group.forEach(item => {
                item.finalX = side === 'left' ? colX - item.w : colX;
                if (item.fixedY !== null) {
                    item.finalY = item.fixedY;
                    item.cy = item.fixedY + item.h / 2;
                } else if (item.alignVertical) {
                    item.finalY = item.boxCy - item.h / 2;
                    item.cy = item.boxCy;
                } else {
                    item.finalY = item.cy - item.h / 2;
                }
            });
        });

        items.forEach(item => {
            item.badge.style.left = `${item.finalX}px`;
            item.badge.style.top = `${item.finalY}px`;
            item.badge.style.visibility = 'visible';
            labelRectsResult.push({ x: item.finalX, y: item.finalY, width: item.w, height: item.h });

            const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            let startX, startY, endX, endY, d;
            const threshold = 5;
            const cornerMargin = 4;
            const cSide = item.def.connectorSide || item.side;

            if (item.side === 'top' || item.side === 'bottom') {
                startX = item.cx;
                startY = item.side === 'top' ? item.finalY + item.h : item.finalY;
                
                if (cSide === 'top') {
                    endX = Math.max(item.box.left + cornerMargin, Math.min(item.box.right - cornerMargin, item.boxCx));
                    endY = item.box.top - 2;
                } else if (cSide === 'bottom') {
                    endX = Math.max(item.box.left + cornerMargin, Math.min(item.box.right - cornerMargin, item.boxCx));
                    endY = item.box.bottom + 2;
                } else if (cSide === 'left') {
                    endX = item.box.left - 2;
                    endY = Math.max(item.box.top + cornerMargin, Math.min(item.box.bottom - cornerMargin, item.boxCy));
                } else {
                    endX = item.box.right + 2;
                    endY = Math.max(item.box.top + cornerMargin, Math.min(item.box.bottom - cornerMargin, item.boxCy));
                }
                
                if (cSide === item.side) {
                    if (Math.abs(startX - endX) < threshold) {
                        d = `M ${endX} ${startY} L ${endX} ${endY}`;
                    } else {
                        const midY = startY + (endY - startY) / 2;
                        d = `M ${startX} ${startY} L ${startX} ${midY} L ${endX} ${midY} L ${endX} ${endY}`;
                    }
                } else {
                    d = `M ${startX} ${startY} L ${startX} ${endY} L ${endX} ${endY}`;
                }
            } else {
                startX = item.side === 'left' ? item.finalX + item.w : item.finalX;
                startY = item.cy;

                if (cSide === 'top') {
                    endX = Math.max(item.box.left + cornerMargin, Math.min(item.box.right - cornerMargin, item.boxCx));
                    endY = item.box.top - 2;
                } else if (cSide === 'bottom') {
                    endX = Math.max(item.box.left + cornerMargin, Math.min(item.box.right - cornerMargin, item.boxCx));
                    endY = item.box.bottom + 2;
                } else if (cSide === 'left') {
                    endX = item.box.left - 2;
                    endY = Math.max(item.box.top + cornerMargin, Math.min(item.box.bottom - cornerMargin, item.boxCy));
                } else {
                    endX = item.box.right + 2;
                    endY = Math.max(item.box.top + cornerMargin, Math.min(item.box.bottom - cornerMargin, item.boxCy));
                }
                
                if (cSide === item.side) {
                    if (Math.abs(startY - endY) < threshold) {
                        d = `M ${startX} ${endY} L ${endX} ${endY}`;
                    } else {
                        const midX = item.connectorMidX !== null ? item.connectorMidX : startX + (endX - startX) / 2;
                        d = `M ${startX} ${startY} L ${midX} ${startY} L ${midX} ${endY} L ${endX} ${endY}`;
                    }
                } else {
                    d = `M ${startX} ${startY} L ${endX} ${startY} L ${endX} ${endY}`;
                }
            }

            path.setAttribute('d', d);
            path.setAttribute('stroke', '#FF8C00');
            path.setAttribute('stroke-width', '2');
            path.setAttribute('fill', 'none');
            svg.appendChild(path);

            console.log(`[Highlight] Label: "${item.def.label}", finalX: ${item.finalX}, finalY: ${item.finalY}, startX: ${startX}, startY: ${startY}, endX: ${endX}, endY: ${endY}, path: ${d}`);
        });
        return labelRectsResult;
    }, defsWithHandles);
}

async function clearHighlights(page) {
    await page.evaluate(() => {
        const overlays = document.querySelectorAll('.playwright-highlight-overlay');
        overlays.forEach(el => el.remove());
    });
}

async function capture(page, pathname, outDir, options = {}) {
    const {
        highlight,
        label,
        clearHighlights: shouldClear = true,
        crop,
        padding = 0,
        percentage,
        insetHighlight = false
    } = options;

    let labelRects = [];

    if (highlight) {
        const highlightDefs = Array.isArray(highlight) && highlight[0] && !highlight[0].click && !highlight[0].elementHandle 
            ? highlight 
            : [{ locators: highlight, label: label, labelSide: options.labelSide, connectorSide: options.connectorSide, inset: insetHighlight }];

        labelRects = await highlightElement(page, highlightDefs, insetHighlight);
        await page.waitForTimeout(100); 
    }

    let rect;
    const boxesToInclude = [];
    if (crop) {
        const locatorArray = Array.isArray(crop) ? crop : [crop];
        for (const loc of locatorArray) {
            const b = await loc.boundingBox();
            if (b) boxesToInclude.push(b);
        }
    }

    if (boxesToInclude.length > 0) {
        const minX = Math.min(...boxesToInclude.map(b => b.x));
        const minY = Math.min(...boxesToInclude.map(b => b.y));
        const maxX = Math.max(...boxesToInclude.map(b => b.x + b.width));
        const maxY = Math.max(...boxesToInclude.map(b => b.y + b.height));
        rect = { x: minX, y: minY, width: maxX - minX, height: maxY - minY };

        if (labelRects.length > 0) {
            const minX2 = Math.min(rect.x, ...labelRects.map(r => r.x));
            const minY2 = Math.min(rect.y, ...labelRects.map(r => r.y));
            const maxX2 = Math.max(rect.x + rect.width, ...labelRects.map(r => r.x + r.width));
            const maxY2 = Math.max(rect.y + rect.height, ...labelRects.map(r => r.y + r.height));
            rect = { x: minX2, y: minY2, width: maxX2 - minX2, height: maxY2 - minY2 };
        }
    } else {
        const size = page.viewportSize() || { width: 1282, height: 720 };
        rect = { x: 0, y: 0, width: size.width, height: size.height };
    }

    const p = typeof padding === 'number' 
        ? { top: padding, right: padding, bottom: padding, left: padding }
        : { top: 0, right: 0, bottom: 0, left: 0, ...padding };

    rect.x -= p.left; rect.y -= p.top; rect.width += p.left + p.right; rect.height += p.top + p.bottom;

    if (percentage) {
        const ops = Array.isArray(percentage) ? percentage : [percentage];
        for (const op of ops) {
            const match = op.match(/(left|right|top|bottom)\s+(\d+)(%|px)/i);
            if (match) {
                const side = match[1].toLowerCase();
                const value = parseInt(match[2], 10);
                const unit = match[3].toLowerCase();

                if (unit === '%') {
                    const factor = value / 100;
                    if (side === 'left') { rect.width *= factor; }
                    else if (side === 'right') { rect.x += rect.width * (1 - factor); rect.width *= factor; }
                    else if (side === 'top') { rect.height *= factor; }
                    else if (side === 'bottom') { rect.y += rect.height * (1 - factor); rect.height *= factor; }
                } else if (unit === 'px') {
                    if (side === 'left') { rect.width = value; }
                    else if (side === 'right') { rect.x += rect.width - value; rect.width = value; }
                    else if (side === 'top') { rect.height = value; }
                    else if (side === 'bottom') { rect.y += rect.height - value; rect.height = value; }
                }
            }
        }
    }

    const fullPath = path.join(outDir, pathname);
    const dir = path.dirname(fullPath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

    await page.screenshot({
        path: fullPath,
        clip: {
            x: Math.max(0, rect.x),
            y: Math.max(0, rect.y),
            width: Math.max(1, rect.width),
            height: Math.max(1, rect.height)
        }
    });

    console.log(`📸 Captured: ${pathname}`);
    if (shouldClear) await clearHighlights(page);
}

async function suppressToasts(page) {
    await page.addStyleTag({ 
        content: `
            div[class*="Snackbar_"], 
            li[class*="Toastify"], 
            div[class*="toast"], 
            div[class*="sonner"],
            #message-dialog-container,
            dialog.message-dialog,
            div[role="status"] { 
                display: none !important; 
                pointer-events: none !important; 
            }
        `
    }).catch(() => {});
}

async function dismissToasts(page) {
    await page.evaluate(() => {
        document.querySelectorAll('div[class*="Snackbar_"], li[class*="Toastify"], div[class*="toast"], div[class*="sonner"], #message-dialog-container, dialog.message-dialog').forEach(el => el.remove());
    }).catch(() => {});
}

module.exports = {
    CONFIG,
    capture,
    highlightElement,
    clearHighlights,
    suppressToasts,
    dismissToasts
};