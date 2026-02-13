from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        self.my_account_dropdown = self.page.locator("a[title='My Account']")
        self.login_button = self.page.locator("//a[text()='Login']")
        self.register_button = self.page.locator("//a[text()='Register']")


