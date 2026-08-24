const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const { CONFIG } = require('./core/capture');

const args = process.argv.slice(2);
let flowName = 'app-lab';
let outDir = path.resolve(__dirname, '../../content/software/app-lab/assets/playwright');
let stepName = 'all';
let debug = false;

for (let i = 0; i < args.length; i++) {
    if (args[i] === '--flow' && args[i + 1]) {
        flowName = args[i + 1];
        i++;
    } else if (args[i] === '--outDir' && args[i + 1]) {
        outDir = path.resolve(process.cwd(), args[i + 1]);
        i++;
    } else if (args[i] === '--step' && args[i + 1]) {
        stepName = args[i + 1];
        i++;
    } else if (args[i] === '--debug' || args[i] === '--verbose') {
        debug = true;
    }
}

if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
}

const debugDir = path.resolve(__dirname, 'debug');
if (!fs.existsSync(debugDir)) {
    fs.mkdirSync(debugDir, { recursive: true });
}

async function run() {
    console.log(`\n🚀 Starting Flow: ${flowName} (Step: ${stepName})`);
    console.log(`📁 Output Directory: ${outDir}`);

    let flowModule;
    try {
        flowModule = require(`./flows/${flowName}.js`);
    } catch (e) {
        console.error(`❌ Flow not found or failed to load: flows/${flowName}.js`);
        console.error(e);
        process.exit(1);
    }

    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({ viewport: CONFIG.viewport, deviceScaleFactor: 1 });
    const page = await context.newPage();
    
    page.on('console', msg => {
        if (msg.text().startsWith('[Highlight]') || msg.text().startsWith('[Box]')) {
            console.log(msg.text());
        }
    });
    
    // Set fast default timeout (3s) for locator queries.
    // Set 30s navigation timeout for page loads.
    page.setDefaultTimeout(3000);
    page.setDefaultNavigationTimeout(30000);
    
    const options = {
        step: stepName,
        debug,
        outDir
    };

    try {
        await page.goto(CONFIG.baseUrl, { timeout: 30000 });
        if (typeof flowModule === 'function') {
            await flowModule(page, outDir, options);
        } else if (flowModule && typeof flowModule.run === 'function') {
            await flowModule.run(page, outDir, options);
        }
        console.log(`\n✅ Flow completed successfully.`);
    } catch (err) {
        console.error(`\n❌ Flow Failed: ${err.message}`);
        
        // Dump DOM and failure info for fast debugging
        try {
            const htmlContent = await page.content();
            const currentUrl = page.url();
            const dumpPath = path.join(debugDir, 'failure-dump.html');
            const logPath = path.join(debugDir, 'failure-details.log');
            
            fs.writeFileSync(dumpPath, htmlContent, 'utf8');
            const logData = `Timestamp: ${new Date().toISOString()}\nURL: ${currentUrl}\nStep: ${stepName}\nError:\n${err.stack || err.message}\n`;
            fs.writeFileSync(logPath, logData, 'utf8');
            console.log(`🔍 Wrote DOM failure dump to: ${dumpPath}`);
            console.log(`🔍 Wrote failure details to: ${logPath}`);
        } catch (dumpErr) {
            console.error(`Could not write failure dump: ${dumpErr.message}`);
        }
    } finally {
        await browser.close();
    }
}

run();
