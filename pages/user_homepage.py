from playwright.sync_api import Page, expect



class UserHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_selector("#content h2")
        self.page.locator("#content h2")


    def verify_user_logged_in(self):
        texts = []
        locators_list = self.page.locator("#content h2").all()
        for i in range(len(locators_list)):
            texts.append(locators_list[i].inner_text())
        return texts

