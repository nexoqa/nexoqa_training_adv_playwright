import { test, expect } from '@playwright/test';
import { faker } from '@faker-js/faker';
import { createUser } from './util';

test('Create new user', async ({ page }) => {
  await page.goto('https://www.demoblaze.com/');
  page.addListener('dialog', (dialog) => {
    expect(dialog.message()).toBe('Sign up successful.');
    dialog.accept();
  });
  let email = faker.internet.email();
  let password = 'Passw0rd!';
  await createUser(page, email, password);
  await page.waitForEvent('dialog');
});
