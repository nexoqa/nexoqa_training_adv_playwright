import { test as setup } from '@playwright/test';
import { login } from '../util';

setup('authenticate', async ({ page }) => {
  await page.goto('https://www.demoblaze.com/');
  await login(page, 'user@arsys.com', '12345678');
  page.context().storageState({ path: './auth.json' });
});
