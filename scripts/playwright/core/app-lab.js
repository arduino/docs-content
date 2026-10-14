// Shared App Lab navigation for Playwright scripts: board selection, Apps page, dialogs,
// App menu, console. Used by flows/app-lab.js; other scripts can require it too.
const { expect } = require('@playwright/test');
const { suppressToasts, dismissToasts } = require('./capture');

/**
 * Selects the connected board on the welcome screen (or keeps the open workspace), and
 * registers handlers that close non-blocking dialogs. Ends on the Apps page.
 * options.board: board name pattern (default UNO Q); options.suppressToasts: hide
 * notifications permanently, as screenshots need (default true).
 */
async function ensureBoardSelected(page, options = {}) {
    const { board = /Arduino UNO Q|UNO Q/i, suppressToasts: hideToasts = true } = options;
    const welcomeBoardCard = page.locator('div[class*="welcome-container"] button, button[class*="board_"]').filter({ hasText: board }).first();
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
    if (hideToasts) await suppressToasts(page);

    // Wait for initial loader to disappear
    await expect(appLoader).toBeHidden({ timeout: 30000 }).catch(() => {});

    // Check if main workspace is already loaded
    if (await page.locator('#my-apps, footer[class*="footer-bar"]').first().isVisible({ timeout: 2000 }).catch(() => false)) {
        console.log('Board already selected and workspace ready.');
        await goToApps(page);
        return;
    }

    // If on welcome screen, verify and select board
    console.log('Checking for connected Arduino UNO Q board...');
    try {
        await welcomeBoardCard.waitFor({ state: 'visible', timeout: 15000 });
        console.log('Board detected!');
        await welcomeBoardCard.click({ force: true });
    } catch (err) {
        throw new Error('Arduino UNO Q board not detected. Please ensure your board is connected and App Lab is running.');
    }

    // Wait until workspace navigation is ready
    try {
        await page.locator('#my-apps, footer[class*="footer-bar"]').first().waitFor({ state: 'visible', timeout: 20000 });
        console.log('Main workspace loaded successfully.');
        await goToApps(page);
    } catch (err) {
        throw new Error('Arduino App Lab workspace failed to load after selecting board.');
    }
}

// App Lab reopens the last workspace on launch, which can be an App editor without the sidebar.
async function goToApps(page) {
    const myAppsButton = page.locator('#my-apps a');
    if (!(await myAppsButton.isVisible({ timeout: 1000 }).catch(() => false))) {
        const appsBreadcrumb = page.locator('nav[aria-label="breadcrumbs"] a, nav[aria-label="breadcrumbs"] button').first();
        if (await appsBreadcrumb.isVisible({ timeout: 1000 }).catch(() => false)) {
            await appsBreadcrumb.click({ force: true });
        }
        await myAppsButton.waitFor({ state: 'visible', timeout: 10000 });
    }
    await myAppsButton.click({ force: true });
    await page.waitForTimeout(1000);
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
    const cancelBtn = page.locator('div[role="dialog"] button').filter({ hasText: /Cancel/i }).first();
    if (await cancelBtn.isVisible({ timeout: 500 }).catch(() => false)) {
        await cancelBtn.click({ force: true }).catch(() => {});
    }
    const closeBtn = page.locator('#close-button, button[class*="close"]').first();
    if (await closeBtn.isVisible({ timeout: 500 }).catch(() => false)) {
        await closeBtn.click({ force: true }).catch(() => {});
    }
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

// The run step leaves the console open, and it covers the lower half of the editor.
async function closeConsole(page) {
    const closeConsoleButton = page.locator('#console button[aria-label="Close"]').first();
    if (await closeConsoleButton.isVisible({ timeout: 1000 }).catch(() => false)) {
        await closeConsoleButton.click({ force: true }).catch(() => {});
        await page.waitForTimeout(500);
    }
}

async function openAppActionsMenu(page) {
    await page.locator('div[class*="app-actions"] button').first().click({ force: true });
    await page.locator('[role="menuitem"]').first().waitFor({ state: 'visible', timeout: 5000 });
    await page.waitForTimeout(300);
}

async function closeDialog(page) {
    const closeButton = page.locator('div[role="dialog"] button[class*="dialog-header-close"]').last();
    if (await closeButton.isVisible({ timeout: 1000 }).catch(() => false)) {
        await closeButton.click({ force: true }).catch(() => {});
    } else {
        await page.keyboard.press('Escape').catch(() => {});
    }
    await page.locator('div[role="dialog"]').last().waitFor({ state: 'hidden', timeout: 5000 }).catch(() => {});
}

// Opens an existing App from the Apps page by its exact name; returns false if it isn't listed.
async function openApp(page, name) {
    await dismissAnyOpenModals(page);
    await goToApps(page);
    // An installed release has a card with the same name; this opens the first match.
    const app = page.locator('div[class*="app-link"]').filter({ has: page.getByText(name, { exact: true }) }).first();
    if (!(await app.isVisible({ timeout: 5000 }).catch(() => false))) return false;
    await app.click({ force: true });
    await page.locator('div[class*="app-actions"]').first().waitFor({ state: 'visible', timeout: 15000 });
    return true;
}

module.exports = {
    ensureBoardSelected,
    goToApps,
    dismissAnyOpenModals,
    stopRunningAppIfAny,
    openApp,
    closeConsole,
    openAppActionsMenu,
    closeDialog,
};
