import { faker } from '@faker-js/faker';
import { test, expect } from '@playwright/test';
import { createUser, login } from './util';

test('Login with new user', async ({ page }) => {
  await page.goto('https://www.demoblaze.com/');
  page.addListener('dialog', (dialog) => {
    dialog.accept();
  });
  let email = faker.internet.email();
  let password = 'Passw0rd!';
  await createUser(page, email, password);
  await page.waitForEvent('dialog');

  await login(page, email, password);

  await expect(page.locator('a#nameofuser')).toHaveText('Welcome ' + email);
});

test.only('Login invalid user', async ({ page }) => {
  await page.goto('https://www.demoblaze.com/');
  page.addListener('dialog', (dialog) => {
    expect(dialog.message()).toBe('User does not exist.');
    dialog.accept();
  });
  let email = faker.internet.email();
  let password = 'Passw0rd!';
  await login(page, email, password);
  await page.waitForEvent('dialog');
});
