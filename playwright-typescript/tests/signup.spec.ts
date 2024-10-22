import { test, expect } from '@playwright/test';
import { faker } from '@faker-js/faker';
import { createUser } from './util';

test('Create new user', async ({ page }) => {
  page.addListener('dialog', (dialog) => {
    expect(dialog.message()).toBe('Sign up successful.');
    dialog.accept();
  });
  let email = faker.internet.email();
  let password = 'Passw0rd!';
  await createUser(page, email, password);
  await page.waitForEvent('dialog');
});

test('Login with new user', async ({ page }) => {
  page.addListener('dialog', (dialog) => {
    // expect(dialog.message()).toBe('Sign up successful.');
    dialog.accept();
  });
  let email = faker.internet.email();
  let password = 'Passw0rd!';
  await createUser(page, email, password);
  await page.waitForEvent('dialog');

  await page.locator('a#login2').click();
  await page.locator('input#loginusername').fill(email);
  await page.locator('input#loginpassword').fill(password);

  await page.getByRole('button', { name: 'Log in' }).click();

  await expect(page.locator('a#nameofuser')).toHaveText('Welcome ' + email);
});
