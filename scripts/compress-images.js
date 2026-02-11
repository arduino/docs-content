const fs = require('fs/promises');
const path = require('path');
const fg = require('fast-glob');
const sharp = require('sharp');
const { optimize } = require('svgo');

const contentDir = path.join(__dirname, '../content');
const imagePattern = '**/*.{png,jpg,jpeg,gif,svg}';

async function compressImages() {
  console.log('Starting image compression...');
  const stream = fg.stream(imagePattern, { cwd: contentDir, absolute: true });

  for await (const entry of stream) {
    try {
      const ext = path.extname(entry).toLowerCase();
      const originalSize = (await fs.stat(entry)).size;

      if (ext === '.svg') {
        const svgString = await fs.readFile(entry, 'utf-8');
        const result = optimize(svgString, {
          path: entry,
          plugins: [
            {
              name: 'preset-default',
              params: {
                overrides: {
                  removeViewBox: false,
                },
              },
            },
          ],
        });
        await fs.writeFile(entry, result.data);
      } else {
        const image = sharp(entry);
        let outputBuffer;
        let outputInfo;

        // Use a temporary file to avoid issues with overwriting the source
        const tempPath = entry + '.tmp';

        switch (ext) {
          case '.png':
            ({ data: outputBuffer, info: outputInfo } = await image
              .png({ quality: 80, compressionLevel: 8, adaptiveFiltering: true })
              .toBuffer({ resolveWithObject: true }));
            break;
          case '.jpg':
          case '.jpeg':
            ({ data: outputBuffer, info: outputInfo } = await image
              .jpeg({ quality: 80, progressive: true, optimizeScans: true })
              .toBuffer({ resolveWithObject: true }));
            break;
          case '.gif':
            console.log(`Skipping GIF optimization for: ${path.relative(contentDir, entry)}`);
            continue;
          default:
            console.log(`Skipping unsupported file type: ${entry}`);
            continue;
        }
        
        if (outputBuffer.length < originalSize) {
            await fs.writeFile(entry, outputBuffer);
            const newSize = outputBuffer.length;
            const reduction = originalSize - newSize;
            const reductionPercent = ((reduction / originalSize) * 100).toFixed(2);
            console.log(
              `Compressed: ${path.relative(contentDir, entry)} | ${formatBytes(originalSize)} -> ${formatBytes(newSize)} (${reductionPercent}%)`
            );
        } else {
            console.log(
              `Skipped (no size reduction): ${path.relative(contentDir, entry)}`
            );
        }
      }
    } catch (error) {
      console.error(`Could not process ${entry}:`, error);
    }
  }

  console.log('Image compression finished.');
}

function formatBytes(bytes, decimals = 2) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

compressImages();
