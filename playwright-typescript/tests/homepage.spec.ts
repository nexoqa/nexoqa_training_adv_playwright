import { test, expect } from '@playwright/test';

test('Validate page title', async ({ page }) => {
  await page.goto('https://www.demoblaze.com/');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/STORE/);
});
