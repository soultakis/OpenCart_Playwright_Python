from playwright.sync_api import Page
from Utils.random_data_generator import RandomData


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

        self.register_page_title = self.page.locator("//h1[text()='Register Account']")
        self.firstname_input = self.page.locator("#input-firstname")
        self.lastname_input = self.page.locator("#input-lastname")
        self.email_input = self.page.locator("#input-email")
        self.phone_input = self.page.locator("#input-telephone")
        self.password_input = self.page.locator("#input-password")
        self.confirm_password_input = self.page.locator("#input-confirm")
        self.accept_terms = self.page.locator("//input[@name='agree']")
        self.continue_button = self.page.locator("//input[@value='Continue']")
        self.yes_bullet = self.page.locator("//label[text()='Yes']")
        self.no_bullet = self.page.locator("//label[text()='No']")
        self.random = RandomData()
        self.success_message = self.page.locator("#content p")
        self.successful_title = self.page.locator("#content h1")
        self.terms_warning_message = self.page.locator("//div[@class='alert alert-danger alert-dismissible']")

    def enter_firstname(self):
        self.firstname_input.fill(self.random.get_firstname())

    def prepare_firstname_validation(self):
        self.fill_all_fields()
        self.accept_the_terms()
        self.firstname_input.clear()

    def enter_firstname_number_of_characters(self, number):
        self.firstname_input.fill(self.random.get_firstname_set_number_of_characters(number))
        self.click_continue()
        return self.success_message.all(), self.successful_title


    # def enter_firstname_minimum_characters(self):
    #     self.firstname_input.fill(self.random.get_firstname_minimum_characters())
    #     self.click_continue()
    #     return self.success_message.all(), self.successful_title

    # def enter_firstname_less_than_minimum(self):
    #     self.firstname_input.fill(self.random.get_firstname_less_than_minimum())
    #     self.click_continue()

    def enter_lastname(self):
        self.lastname_input.fill(self.random.get_lastname())

    def enter_email(self):
        self.email_input.fill(self.random.get_email())

    def enter_phone(self):
        self.phone_input.fill(self.random.get_phone_number())

    def enter_password(self):
        password = self.random.get_password()
        self.password_input.fill(password)
        return password

    def confirm_password(self, password):
        self.confirm_password_input.fill(password)

    def accept_the_terms(self):
        self.accept_terms.check()

    def click_continue(self):
        self.continue_button.click()

    def fill_all_fields(self):
        self.enter_firstname()
        self.enter_lastname()
        self.enter_email()
        self.enter_phone()
        password = self.enter_password()
        self.confirm_password(password)

    def submit_registration_form(self, subscribe = False):
        self.fill_all_fields()
        if subscribe:
            self.yes_bullet.check()
        else:
            self.no_bullet.check()
        self.accept_the_terms()
        self.click_continue()

    # def submit_empty_form(self):
    #     self.continue_button.click()
    #     # return self.terms_warning_message, self.firstname_error_message

    # def validate_each_field_that_is_empty(self):
    #     self.fill_all_fields()
    #     self.accept_the_terms()
        



