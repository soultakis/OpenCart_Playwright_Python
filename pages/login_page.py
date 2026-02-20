from playwright.sync_api import Page
from variables import *

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_address_input = self.page.locator("#input-email")
        self.password_input = self.page.locator("#input-password")
        self.login_button = self.page.locator("input[value='Login']")
        self.invalid_login_warning = self.page.locator("//div[@class='alert alert-danger alert-dismissible']")

        self.right_side_menu_items = self.page.locator("a[class = 'list-group-item']")

    def set_email_address(self,email):
        self.email_address_input.fill(email)

    def set_user_login_password(self,password):
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login_procedure(self, email, password):
        self.set_email_address(email)
        self.set_user_login_password(password)
        self.click_login_button()







