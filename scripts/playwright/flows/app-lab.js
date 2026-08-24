const fs = require('fs');
const path = require('path');
const { expect } = require('@playwright/test');
const { capture, suppressToasts, dismissToasts } = require('../core/capture');

async function ensureBoardSelected(page) {
    const welcomeBoardCard = page.locator('div[class*="welcome-container"] button, button[class*="board_"]').filter({ hasText: /Arduino UNO Q|UNO Q/i }).first();
    const appLoader = page.locator('div[class*="arduino-loader"]');

    // Register handlers for non-blocking dialogs
    const closeWarningDialogButton = page.locator('#close-button');
    const remindMeLaterButton = page.getByRole('button', { name: 'Remind me later' });
    const confirmAndReplaceButton = page.getByRole('button', { name: 'Confirm and replace' });
    const okGotItButton = page.getByRole('button', { name: /Ok, got it|Get started/i });

    page.addLocatorHandler(closeWarningDialogButton, async () => {
        await closeWarningDialogButton.click().catch(() => {});
    });

    page.addLocatorHandler(remindMeLaterButton, async () => {
        await remindMeLaterButton.click().catch(() => {});
    });

    page.addLocatorHandler(confirmAndReplaceButton, async () => {
        await confirmAndReplaceButton.click().catch(() => {});
    });

    page.addLocatorHandler(okGotItButton, async () => {
        await okGotItButton.click().catch(() => {});
    });

    // Permanently suppress toasts from appearing in screenshots
    await suppressToasts(page);

    // Wait for initial loader to disappear
    await expect(appLoader).toBeHidden({ timeout: 30000 }).catch(() => {});

    // Check if main workspace is already loaded
    if (await page.locator('#my-apps, footer[class*="footer-bar"]').first().isVisible({ timeout: 2000 }).catch(() => false)) {
        console.log('Board already selected and workspace ready.');
        return;
    }

    // If on welcome screen, verify and select board
    console.log('Checking for connected Arduino UNO Q board...');
    try {
        await welcomeBoardCard.waitFor({ state: 'visible', timeout: 45000 });
        console.log('Board detected!');
        await welcomeBoardCard.click({ force: true });
    } catch (err) {
        throw new Error('Arduino UNO Q board not detected. Please ensure your board is connected and App Lab is running.');
    }

    // Wait until workspace navigation is ready
    try {
        await page.locator('#my-apps, footer[class*="footer-bar"]').first().waitFor({ state: 'visible', timeout: 20000 });
        console.log('Main workspace loaded successfully.');
    } catch (err) {
        throw new Error('Arduino App Lab workspace failed to load after selecting board.');
    }
}

async function dismissAnyOpenModals(page) {
    const remindMeLater = page.getByRole('button', { name: 'Remind me later' }).first();
    if (await remindMeLater.isVisible({ timeout: 500 }).catch(() => false)) {
        await remindMeLater.click({ force: true }).catch(() => {});
    }
    const okGotIt = page.getByRole('button', { name: /Ok, got it|Get started/i }).first();
    if (await okGotIt.isVisible({ timeout: 500 }).catch(() => false)) {
        await okGotIt.click({ force: true }).catch(() => {});
    }
    const closeBtn = page.locator('#close-button').first();
    if (await closeBtn.isVisible({ timeout: 500 }).catch(() => false)) {
        await closeBtn.click({ force: true }).catch(() => {});
    }
    await page.evaluate(() => {
        document.querySelectorAll('div[class*="Modal--overlay"], div[role="dialog"]').forEach(el => el.remove());
        document.body.style.pointerEvents = 'auto';
        document.body.removeAttribute('data-scroll-locked');
        document.documentElement.style.pointerEvents = 'auto';
    }).catch(() => {});
}

async function stopRunningAppIfAny(page) {
    const stopButtonBottom = page.locator('footer[class*="footer-bar"] button').filter({ hasText: 'Stop' }).first();
    if (await stopButtonBottom.isVisible({ timeout: 1000 }).catch(() => false)) {
        console.log('Stopping currently running app...');
        await stopButtonBottom.click({ force: true }).catch(() => {});
        await expect(stopButtonBottom).toBeHidden({ timeout: 30000 }).catch(() => {});
        await dismissToasts(page);
    }
}

async function cleanupExistingAwesomeApp(page) {
    const myAppsButton = page.locator('#my-apps a');
    if (await myAppsButton.isVisible({ timeout: 2000 }).catch(() => false)) {
        await myAppsButton.click({ force: true }).catch(() => {});
        await page.waitForTimeout(500);
        
        // Wait for apps to finish loading
        await page.locator('div[class*="app-link"], div[class*="empty-state"]').first().waitFor({ state: 'visible', timeout: 10000 }).catch(() => {});
        await page.waitForTimeout(500);

        const existingApp = page.locator('div[class*="app-link"]').filter({ hasText: /AwesomeApp/i }).first();
        if (await existingApp.isVisible({ timeout: 2000 }).catch(() => false)) {
            console.log('Removing previous AwesomeApp instance...');
            await existingApp.click({ force: true }).catch(() => {});
            await page.waitForTimeout(1000);
            const appMenuTrigger = page.locator('div[class*="app-actions"] button').first();
            if (await appMenuTrigger.isVisible({ timeout: 3000 }).catch(() => false)) {
                await appMenuTrigger.click({ force: true }).catch(() => {});
                await page.waitForTimeout(500);
                const deleteMenuItem = page.locator('[role="menuitem"]').filter({ hasText: /Delete/i }).first();
                if (await deleteMenuItem.isVisible({ timeout: 2000 }).catch(() => false)) {
                    await deleteMenuItem.click({ force: true }).catch(() => {});
                    await page.waitForTimeout(500);
                    const confirmDeleteBtn = page.locator('div[role="dialog"] button[type="submit"], div[role="dialog"] button').filter({ hasText: /Delete/i }).last();
                    if (await confirmDeleteBtn.isVisible({ timeout: 2000 }).catch(() => false)) {
                        await confirmDeleteBtn.click({ force: true }).catch(() => {});
                        await page.waitForTimeout(1500);
                    }
                }
            }
            await myAppsButton.click({ force: true }).catch(() => {});
            await page.waitForTimeout(1000);
        }
    }
}

module.exports = async function runAppLabFlow(page, outDir, options = {}) {
    const { step = 'all' } = options;

    // 1. Initial State Preparation
    await ensureBoardSelected(page);
    await dismissAnyOpenModals(page);
    await stopRunningAppIfAny(page);
    await suppressToasts(page);

    // ==========================================
    // LOCATORS
    // ==========================================
    const statusbar = page.locator('footer[class*="footer-bar"]').last();
    const boardSwitchControl = page.locator('[class*="_selected-board"]').last().locator('..');
    const openTerminalButton = page.locator('button[aria-label*="Connect to the board"]').first();
    const systemStatus = page.locator('div[class*="_footer-section--center"]').first();
    const notificationsButton = page.locator('div[class*="notification-icon-container"]').last();
    const networkButton = page.locator('div[class*="network-icon-container"]').last();
    const agentModeButton = statusbar.locator('div[class*="ai-assistant-entry"] button, button[aria-label*="Agent Mode"], button[aria-label*="Editor Mode"]').first();

    // Navigation rows
    const myAppsButton = page.locator('#my-apps a');
    const inspirationsButton = page.locator('#inspirations a');
    const examplesButton = page.locator('#examples a');
    const learnButton = page.locator('#resources a');
    const bricksButton = page.locator('#bricks a');
    const settingsButton = page.locator('button[aria-label="Settings"]').first();
    const accountButton = page.locator('button[aria-label="Account"]').first();
    const settingsBackButton = page.getByRole('button', { name: 'Settings' }).first();

    const sidebar = page.locator('nav, aside, div[class*="side-panel"], div[class*="sidebar"]').first();

    // ==========================================
    // STEP: NAVIGATION & STATUS BAR
    // ==========================================
    if (step === 'all' || step === 'navigation') {
        console.log('\n--- Step: Navigation & Status Bar ---');
        
        try {
            await capture(page, 'config/board-selection.png', outDir, { percentage: 'top 75%' });
        } catch (e) {
            console.log('Board selection screenshot skipped.');
        }

        try {
            await capture(page, 'sidebar-hl.png', outDir, { highlight: sidebar, insetHighlight: true });
        } catch (e) {
            console.log('Full sidebar highlight skipped.');
        }

        // 1. Full sidebar with top group outlined (no labels) and bottom items labeled
        await capture(page, 'navigation/sidebar-icons-hl.png', outDir, {
            highlight: [
                { locators: [myAppsButton, inspirationsButton, examplesButton, learnButton, bricksButton] },
                { 
                    locators: accountButton, 
                    label: 'ACCOUNT', 
                    labelSide: 'right', 
                    connectorSide: 'right',
                    fixedY: 575,
                    connectorMidX: 100
                },
                { 
                    locators: settingsButton, 
                    label: 'SETTINGS', 
                    labelSide: 'right', 
                    connectorSide: 'right',
                    alignVertical: true
                }
            ]
        });

        // 2. Subset: Top navigation options only (single border, no labels)
        await capture(page, 'navigation/sidebar-nav-hl.png', outDir, {
            highlight: [
                { locators: [myAppsButton, inspirationsButton, examplesButton, learnButton, bricksButton] }
            ]
        });

        // 3. Subset: Bottom options only (Account and Settings, single border, no labels)
        await capture(page, 'navigation/sidebar-settings-account-hl.png', outDir, {
            highlight: [
                { locators: [accountButton, settingsButton] }
            ]
        });

        await capture(page, 'navigation/sidebar-icons-hl-crop.png', outDir, {
            highlight: [
                { locators: [myAppsButton, inspirationsButton, examplesButton, learnButton, bricksButton] },
                { 
                    locators: accountButton, 
                    label: 'ACCOUNT', 
                    labelSide: 'right', 
                    connectorSide: 'right',
                    fixedY: 575,
                    connectorMidX: 100
                },
                { 
                    locators: settingsButton, 
                    label: 'SETTINGS', 
                    labelSide: 'right', 
                    connectorSide: 'right',
                    alignVertical: true
                }
            ],
            percentage: 'left 40%'
        });

        await capture(page, 'statusbar-hl.png', outDir, { highlight: statusbar, insetHighlight: true });
        await capture(page, 'statusbar-board-hl.png', outDir, { highlight: boardSwitchControl, insetHighlight: false, percentage: 'bottom 115px' });

        await capture(page, 'statusbar-controls-hl.png', outDir, {
            highlight: [
                { locators: boardSwitchControl, label: 'BOARD', labelSide: 'top', connectorSide: 'top' },
                { locators: openTerminalButton, label: 'TERMINAL', labelSide: 'top', connectorSide: 'top' },
                { locators: systemStatus, label: 'STATUS', labelSide: 'top', connectorSide: 'top' },
                { locators: notificationsButton, label: 'NOTIFICATIONS', labelSide: 'top', connectorSide: 'top' },
                { locators: networkButton, label: 'NETWORK', labelSide: 'top', connectorSide: 'top' },
                { locators: agentModeButton, label: 'AGENT MODE', labelSide: 'top', connectorSide: 'top' }
            ],
            percentage: 'bottom 25%'
        });

        await capture(page, 'statusbar-crop.png', outDir, { crop: statusbar });

        // Tab transitions
        await myAppsButton.click({ force: true });
        await page.waitForTimeout(500);
        await capture(page, 'navigation/sidebar-hl-my-apps.png', outDir, { highlight: myAppsButton });

        await inspirationsButton.click({ force: true });
        await page.waitForTimeout(500);
        await capture(page, 'navigation/sidebar-hl-inspirations.png', outDir, { highlight: inspirationsButton });

        await examplesButton.click({ force: true });
        await page.waitForTimeout(500);
        await capture(page, 'navigation/sidebar-hl-examples.png', outDir, { highlight: examplesButton });

        await learnButton.click({ force: true });
        await page.waitForTimeout(500);
        await capture(page, 'navigation/sidebar-hl-learn.png', outDir, { highlight: learnButton });

        await settingsButton.click({ force: true });
        await page.waitForTimeout(500);
        await capture(page, 'navigation/sidebar-hl-settings.png', outDir, {});
        if (await settingsBackButton.isVisible({ timeout: 1000 }).catch(() => false)) {
            await settingsBackButton.click({ force: true }).catch(() => {});
        }

        await accountButton.click({ force: true });
        await page.waitForTimeout(500);
        await capture(page, 'navigation/sidebar-hl-account.png', outDir, { highlight: accountButton });
    }

    // ==========================================
    // STEP: INSPIRATIONS
    // ==========================================
    if (step === 'all' || step === 'inspirations') {
        console.log('\n--- Step: Inspirations ---');
        await inspirationsButton.click({ force: true });
        await page.waitForTimeout(1000);

        // Find the Blink card in Inspirations
        const blinkCard = page.locator('div[class*="app-link"]').filter({ hasText: /Blink/i }).first();
        await blinkCard.waitFor({ state: 'visible', timeout: 10000 });
        await blinkCard.click({ force: true });
        await page.waitForTimeout(1000);

        const runButton = page.locator('button').filter({ hasText: 'Run' }).first();
        const copyExampleButton = page.locator('button').filter({ hasText: 'Copy and edit app' }).first();
        const rootBreadcrumb = page.locator('nav[aria-label="breadcrumbs"] a, nav[aria-label="breadcrumbs"] button').first();

        await capture(page, 'inspirations/blink-led-run.png', outDir, { highlight: runButton, percentage: 'top 25%' });
        await capture(page, 'inspirations/blink-led-copy.png', outDir, { highlight: copyExampleButton, percentage: 'top 25%' });
        
        await rootBreadcrumb.click({ force: true });
        await page.waitForTimeout(500);
    }

    // ==========================================
    // STEP: EDITOR & APP CREATION
    // ==========================================
    if (step === 'all' || step === 'editor' || step === 'run') {
        console.log('\n--- Step: Editor & App Creation ---');
        await cleanupExistingAwesomeApp(page);

        await myAppsButton.click({ force: true });
        await page.waitForTimeout(500);

        // Open create app dialog
        const createAppDropdown = page.locator('button').filter({ hasText: /Create new app|Create App/i }).first();
        await createAppDropdown.click({ force: true });
        await page.waitForTimeout(300);
        const createAppMenuItem = page.locator('[role="menuitem"]').filter({ hasText: /Create/i }).first();
        if (await createAppMenuItem.isVisible({ timeout: 1000 }).catch(() => false)) {
            await createAppMenuItem.click({ force: true });
            await page.waitForTimeout(500);
        }

        // Fill dialog
        const nameInput = page.getByRole('textbox').first();
        await nameInput.fill('AwesomeApp');

        // Emoji picker - select and assert rocket emoji
        console.log('Opening emoji picker dialog...');
        const emojiButton = page.locator('div[role="dialog"] button[class*="emoji-picker-button"]').first();
        await emojiButton.waitFor({ state: 'visible', timeout: 5000 });
        await emojiButton.click({ force: true });
        await page.waitForTimeout(500);

        // Click category tab "Travel & Places"
        const travelPlacesTab = page.locator('button.epr-cat-travel-places, [aria-label*="Travel & Places"]').or(page.getByRole('tab', { name: /Travel & Places/i })).first();
        if (await travelPlacesTab.isVisible({ timeout: 2000 }).catch(() => false)) {
            console.log('Selecting Travel & Places category...');
            await travelPlacesTab.click({ force: true });
            await page.waitForTimeout(300);
        }

        // Locate rocket emoji button
        const rocketEmojiBtn = page.locator('button.epr-emoji[data-unified="1f680"], button[aria-label*="rocket"], button:has(img[src*="1f680"])').first();
        
        try {
            await rocketEmojiBtn.scrollIntoViewIfNeeded({ timeout: 3000 });
        } catch (e) {
            const emojiList = page.locator('.epr-body, .epr-emoji-list').first();
            if (await emojiList.isVisible()) {
                await emojiList.focus().catch(() => {});
                for (let s = 0; s < 10; s++) {
                    if (await rocketEmojiBtn.isVisible().catch(() => false)) break;
                    await page.keyboard.press('PageDown').catch(() => {});
                    await page.waitForTimeout(100);
                }
            }
        }

        await rocketEmojiBtn.waitFor({ state: 'visible', timeout: 5000 });
        console.log('Clicking rocket emoji...');
        await rocketEmojiBtn.click({ force: true });
        await page.waitForTimeout(500);

        // ASSERTION: Verify the dialog's emoji picker button now displays the rocket emoji
        const dialogEmojiImg = page.locator('div[role="dialog"] button[class*="emoji-picker-button"] img[src*="1f680"], div[role="dialog"] button[class*="emoji-picker-button"] img[alt*="rocket"]');
        await expect(dialogEmojiImg).toBeVisible({ timeout: 5000 });
        console.log('✅ Confirmed: Rocket emoji is configured in Create App dialog.');

        const confirmCreateBtn = page.locator('button[type="submit"]').filter({ hasText: /Create new|Confirm/i }).first();
        await confirmCreateBtn.click({ force: true });
        await dismissToasts(page);
        await page.waitForTimeout(2000);

        // ASSERTION: Verify the editor top bar displays AwesomeApp with the rocket emoji
        const topBarAppEmoji = page.locator('div[class*="app-title"] button[class*="emoji-picker-button"] img[src*="1f680"], div[class*="app-title"] button[class*="emoji-picker-button"] img[alt*="rocket"]');
        await expect(topBarAppEmoji).toBeVisible({ timeout: 15000 });
        console.log('✅ Confirmed: Editor top bar displays AwesomeApp with Rocket emoji.');

        // Editor Elements
        const appActionsButton = page.locator('div[class*="app-actions"]').first();
        const emojiPickerButton = page.locator('button[class*="emoji-picker-button"]').first();
        const editorSidePanel = page.locator('#side');
        const breadcrumbs = page.locator('nav[aria-label="breadcrumbs"]').first();
        const runButton = page.locator('button').filter({ hasText: 'Run' }).first();

        const addBrickButton = page.locator('button[aria-label="Add Brick"]').first();
        const addLibraryButton = page.locator('button[aria-label="Add Sketch Library"]').first();
        const addFileButton = page.locator('button[aria-label="Add File"]').first();

        const sketchFolder = page.locator('div[role="treeitem"]').filter({ hasText: /^sketch$/i }).first();
        const pythonFolder = page.locator('div[role="treeitem"]').filter({ hasText: /^python$/i }).first();
        const mainPyFile = page.locator('div[role="treeitem"]').filter({ hasText: /main\.py/i }).first();
        const sketchFile = page.locator('div[role="treeitem"]').filter({ hasText: /sketch\.ino/i }).first();
        const appYamlFile = page.locator('div[role="treeitem"]').filter({ hasText: /app\.yaml/i }).first();

        const tabsList = page.locator('ul[class*="tabs-list"]');
        const mainPyTab = tabsList.locator('[data-file-id*="main.py"]').first();

        await capture(page, 'editor/editor.png', outDir, {});
        await capture(page, 'editor/app-actions-button.png', outDir, { highlight: appActionsButton, percentage: 'top 25%' });
        await capture(page, 'editor/emoji-picker-button.png', outDir, { highlight: emojiPickerButton, percentage: 'top 25%' });

        if (await pythonFolder.isVisible({ timeout: 1000 }).catch(() => false)) {
            await pythonFolder.click({ force: true }).catch(() => {});
        }
        if (await sketchFolder.isVisible({ timeout: 1000 }).catch(() => false)) {
            await sketchFolder.click({ force: true }).catch(() => {});
        }

        await capture(page, 'editor/editor-folders-expanded.png', outDir, {});
        await capture(page, 'editor/editor-folders-expanded-sidepanel-hl.png', outDir, { highlight: editorSidePanel, insetHighlight: true });
        await capture(page, 'editor/editor-folders-expanded-files-hl.png', outDir, { highlight: [pythonFolder, appYamlFile], insetHighlight: false, percentage: 'top 75%' });

        // Edit Code in Sketch and Python
        const editorInput = page.getByRole('textbox').first();
        if (await mainPyFile.isVisible({ timeout: 1000 }).catch(() => false)) {
            await mainPyFile.click({ force: true }).catch(() => {});
            await editorInput.focus().catch(() => {});
            await editorInput.press('Space').catch(() => {});
            await editorInput.press('Backspace').catch(() => {});
        }

        if (await sketchFile.isVisible({ timeout: 1000 }).catch(() => false)) {
            await sketchFile.click({ force: true }).catch(() => {});
            const sketchPath = path.join(__dirname, '../sketch.ino');
            if (fs.existsSync(sketchPath)) {
                const sketchCode = fs.readFileSync(sketchPath, 'utf8');
                await editorInput.focus().catch(() => {});
                await page.keyboard.press('ControlOrMeta+A').catch(() => {});
                await page.keyboard.insertText(sketchCode).catch(() => {});
                await page.waitForTimeout(500);
            }
        }

        if (await mainPyTab.isVisible({ timeout: 1000 }).catch(() => false)) {
            await mainPyTab.click({ force: true }).catch(() => {});
        }

        await capture(page, 'editor/add-brick-button.png', outDir, { highlight: addBrickButton, percentage: 'top 25%' });
        await capture(page, 'editor/add-library-button.png', outDir, { highlight: addLibraryButton, percentage: 'top 25%' });
        await capture(page, 'editor/add-file-button.png', outDir, { highlight: addFileButton, percentage: 'top 25%' });

        await capture(page, 'editor/topbar-hl.png', outDir, { highlight: [breadcrumbs, runButton] });
        await capture(page, 'editor/top-half.png', outDir, { percentage: 'top 50%' });

        // ==========================================
        // STEP: RUN & CONSOLE
        // ==========================================
        if (step === 'all' || step === 'run') {
            console.log('\n--- Step: App Execution & Console ---');
            await capture(page, 'editor/run-button.png', outDir, { highlight: runButton, percentage: 'top 25%' });
            
            console.log('Starting app execution on live board...');
            await runButton.click({ force: true });

            // Wait for app to start running on the live board
            const stopButtonTop = page.locator('div[class*="top-bar"] button').filter({ hasText: 'Stop' }).first();
            const stopButtonBottom = statusbar.locator('button').filter({ hasText: 'Stop' }).first();
            const runningAppBottom = statusbar.locator('div[class*="app-name-container"]').first();

            console.log('Waiting for app compilation and launch on board...');
            await stopButtonTop.waitFor({ state: 'visible', timeout: 90000 });
            await page.waitForTimeout(3000);

            await capture(page, 'editor/stop-button.png', outDir, { highlight: stopButtonTop, percentage: 'top 25%' });
            if (await stopButtonBottom.isVisible({ timeout: 5000 }).catch(() => false)) {
                await capture(page, 'editor/stop-button-bottom.png', outDir, { highlight: stopButtonBottom, percentage: 'bottom 25%' });
            }
            if (await runningAppBottom.isVisible({ timeout: 10000 }).catch(() => false)) {
                await capture(page, 'editor/running-app-bottom.png', outDir, { highlight: runningAppBottom, percentage: 'bottom 50%' });
            }

            // Console Panel
            const consolePanel = page.locator('#console');
            const consoleHeader = consolePanel.locator('div[class*="console-panel-header_"]').or(consolePanel.locator('header')).first();
            const consoleTabSerialMonitor = consolePanel.getByRole('button', { name: /Serial Monitor/i }).first();

            await capture(page, 'editor/console-panel.png', outDir, { percentage: 'bottom 50%' });
            await capture(page, 'editor/console-panel-hl.png', outDir, { highlight: consolePanel, insetHighlight: true });
            await capture(page, 'editor/console/console-panel-hl-50%.png', outDir, { highlight: consolePanel, insetHighlight: true, percentage: 'bottom 50%' });
            await capture(page, 'editor/console/console-header-hl.png', outDir, { highlight: consoleHeader, insetHighlight: true, percentage: 'bottom 50%' });

            if (await consoleTabSerialMonitor.isVisible({ timeout: 2000 }).catch(() => false)) {
                await consoleTabSerialMonitor.click({ force: true }).catch(() => {});
                await page.waitForTimeout(3000);
                await capture(page, 'editor/console/console-panel-serial-hl.png', outDir, { highlight: consolePanel, insetHighlight: true, percentage: 'bottom 50%' });
            }

            // Clean up: stop the app
            await stopRunningAppIfAny(page);
        }
    }
};
