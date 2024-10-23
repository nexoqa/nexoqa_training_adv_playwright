import { expect, Page } from '@playwright/test';

export async function createUser(page: Page, user: string, password: string) {
  await page.locator('a#signin2').click();

  await page.locator('input#sign-username').fill(user);
  await page.locator('input#sign-password').fill(password);

  await page.getByRole('button', { name: 'Sign up' }).click();
}

export async function login(page: Page, user: string, password: string) {
  await page.locator('a#login2').click();
  await page.locator('input#loginusername').fill(user);
  await page.locator('input#loginpassword').fill(password);
  await page.getByRole('button', { name: 'Log in' }).click();
}
