from playwright.sync_api import Page, expect
from conftest import go_to_register_page
from pages.registration_error_locators import RegistrationErrorLocators
from variables import *
from pages.registration_error_locators import RegistrationErrorLocators


def test_firstname_validate_firstname_minimum_length(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_firstname_validation()
    success_message, success_title = register_page.enter_firstname_minimum_characters()

    assert success_title.inner_text() == registration_success_title
    for i in range(len(success_message)):
        assert success_message[i].inner_text() == registration_success_messages[i]


def test_empty_firstname_validation(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_firstname_validation()
    register_page.click_continue()
    registration_errors = RegistrationErrorLocators(page)
    expect(registration_errors.firstname_error_message).to_have_text(registration_firstname_error_message)


def test_firstname_validate_firstname_length_less_than_minimum(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_firstname_validation()
    register_page.enter_firstname_less_than_minimum()
    registration_errors = RegistrationErrorLocators(page)
    expect(registration_errors.firstname_error_message).to_be_visible()
    expect(registration_errors.firstname_error_message).to_have_text(registration_firstname_error_message)









