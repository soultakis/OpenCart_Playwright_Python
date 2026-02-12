from playwright.sync_api import Page
from variables import *

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_address_input = self.page.locator("#input-email")
        self.password_input = self.page.locator("#input-password")
        self.login_button = self.page.locator("input[value='Login']")


    def login_success(self):
        self.email_address_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()


