import { faker } from '@faker-js/faker';
import { test, expect } from '@playwright/test';
import { createUser, login } from './util';

test.only('Add product to shopping car', async ({ page }) => {
  page.addListener('dialog', (dialog) => {
    if (dialog.message() == 'Sign up successful.') {
      dialog.accept();
    } else {
      expect(dialog.message()).toBe('Product added.');
      dialog.accept();
    }
  });
  await page.goto('https://www.demoblaze.com/');
  let email = faker.internet.email();
  let password = 'Passw0rd!';
  await createUser(page, email, password);
  await page.waitForEvent('dialog');
  await login(page, email, password);

  await page.locator('div#tbodyid div.card h4.card-title a').nth(0).click();

  await page.getByRole('link', { name: 'Add to cart' }).click();

  await page.waitForEvent('dialog');
});
