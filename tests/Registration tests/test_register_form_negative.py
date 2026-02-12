from playwright.sync_api import Page, expect
from conftest import go_to_register_page
from variables import *
from pages.registration_error_locators import RegistrationErrorLocators


def test_register_submit_empty_form(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.submit_empty_form()
    registration_errors = RegistrationErrorLocators(page)

    expect(page).to_have_url(registration_page_url)
    expect(registration_errors.terms_warning_message).to_have_text(registration_terms_warning_message)
    expect(registration_errors.firstname_error_message).to_have_text(registration_firstname_error_message)
    expect(registration_errors.lastname_error_message).to_have_text(registration_lastname_error_message)
    expect(registration_errors.email_error_message).to_have_text(registration_email_error_message)
    expect(registration_errors.telephone_error_message).to_have_text(registration_telephone_error_message)
    expect(registration_errors.password_error_message).to_have_text(registration_password_error_message)


# def test_validate_empty_fields(page: Page, go_to_register_page):
#     register_page = go_to_register_page
#     register_page.validate_each_field_that_is_empty()
