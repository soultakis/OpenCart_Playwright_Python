from playwright.sync_api import Page, expect

class MyAccount:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_selector("#content h2")
        self.page.locator("#content h2")


    def read_successful_logged_in_messages(self):
        locators_list = self.page.locator("#content h2").all()
        return locators_list


