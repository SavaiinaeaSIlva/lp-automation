const { test, expect } = require('@playwright/test');

test('take full page screenshot', async ({ page }) => {
  await page.goto('http://localhost:8000');
  await page.screenshot({ path: 'redesign_screenshot.png', fullPage: true });
});
