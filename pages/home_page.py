from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        self.my_account_dropdown = self.page.locator("a[title='My Account']")
        self.login_button = self.page.locator("//a[text()='Login']")
        self.register_button = self.page.locator("//a[text()='Register']")
        self.search_input_field = self.page.locator("input[name='search']")
        self.search_button = self.page.locator("i[class='fa fa-search']")

    def click_my_account_dropdown(self):
        self.my_account_dropdown.click()

    def click_login_button(self):
        self.login_button.click()

    def click_register_button(self):
        self.register_button.click()

    def enter_search_text(self, search_text):
        self.search_input_field.fill(search_text)

    def click_search_button(self):
        self.search_button.click()




