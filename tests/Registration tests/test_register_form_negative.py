from playwright.sync_api import Page, expect
from conftest import go_to_register_page
from variables import *
from pages.registration_error_locators import RegistrationErrorLocators


def test_register_submit_empty_form(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.click_continue()
    registration_errors = RegistrationErrorLocators(page)

    expect(page).to_have_url(registration_page_url)
    expect(registration_errors.terms_warning_message).to_have_text(registration_terms_warning_message)
    expect(registration_errors.firstname_error_message).to_have_text(registration_firstname_error_message)
    expect(registration_errors.lastname_error_message).to_have_text(registration_lastname_error_message)
    expect(registration_errors.email_error_message).to_have_text(registration_email_error_message)
    expect(registration_errors.telephone_error_message).to_have_text(registration_telephone_error_message)
    expect(registration_errors.password_error_message).to_have_text(registration_password_error_message)


def test_validate_do_not_accept_terms(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.fill_all_fields()
    register_page.click_continue()
    expect(page).to_have_url(registration_page_url)
    expect(register_page.terms_warning_message).to_have_text(registration_terms_warning_message)

def test_validate_each_field_is_empty(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.fill_all_fields()

