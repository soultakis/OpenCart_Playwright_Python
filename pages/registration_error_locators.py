from playwright.sync_api import Page
from Utils.random_data_generator import RandomData

class RegistrationErrorLocators:
    def __init__(self, page: Page):
        self.page = page

        self.terms_warning_message = self.page.locator("//div[@class='alert alert-danger alert-dismissible']")
        self.firstname_error_message = self.page.locator("#input-firstname + .text-danger")
        self.lastname_error_message = self.page.locator("#input-lastname + .text-danger")
        self.email_error_message = self.page.locator("#input-email + .text-danger")
        self.telephone_error_message = self.page.locator("#input-telephone + .text-danger")
        self.password_error_message = self.page.locator("#input-password + .text-danger")
