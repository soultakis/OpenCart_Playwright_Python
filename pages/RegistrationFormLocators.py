from playwright.sync_api import Page

class RegisterFormLocators:
    def __init__(self, page: Page):
        self.page = page

        self.firstname_input = self.page.locator("#input-firstname")
        self.lastname_input = self.page.locator("#input-lastname")
        self.email_input = self.page.locator("#input-email")
        self.phone_input = self.page.locator("#input-telephone")
        self.password_input = self.page.locator("#input-password")
        self.confirm_password_input = self.page.locator("#input-confirm")
        self.accept_terms = self.page.locator("//input[@name='agree']")
        self.continue_button = self.page.locator("//input[@value='Continue']")

        self.registration_input_fields = [self.firstname_input,
                                          self.lastname_input,
                                          self.email_input,
                                          self.phone_input,
                                          self.password_input,
                                          self.confirm_password_input]

