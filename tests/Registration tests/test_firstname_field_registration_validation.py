from playwright.sync_api import Page, expect
from conftest import go_to_register_page
from pages.registration_error_locators import RegistrationErrorLocators
from variables import *
from pages.registration_error_locators import RegistrationErrorLocators


def test_firstname_validate_firstname_minimum_length(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_firstname_validation()
    register_page.enter_firstname_number_of_characters(min_length_input)
    expect(register_page.successful_title).to_have_text(registration_success_title)
    for i in range(len(register_page.success_message.all())):
        expect(register_page.success_message.all()[i]).to_have_text(registration_success_messages[i])


def test_firstname_validate_firstname_maximum_length(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_firstname_validation()
    register_page.enter_firstname_number_of_characters(max_length_input)
    expect(register_page.successful_title).to_have_text(registration_success_title)
    for i in range(len(register_page.success_message.all())):
        expect(register_page.success_message.all()[i]).to_have_text(registration_success_messages[i])

def test_empty_firstname_validation(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_firstname_validation()
    register_page.click_continue()
    registration_errors = RegistrationErrorLocators(page)
    expect(registration_errors.firstname_error_message).to_have_text(registration_firstname_error_message)

def test_firstname_validate_firstname_length_less_than_minimum(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_firstname_validation()
    register_page.enter_firstname_number_of_characters(less_than_min_length_input)
    registration_errors = RegistrationErrorLocators(page)
    expect(registration_errors.firstname_error_message).to_be_visible()
    expect(registration_errors.firstname_error_message).to_have_text(registration_firstname_error_message)

def test_firstname_validate_firstname_length_more_than_maximum(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_firstname_validation()
    register_page.enter_firstname_number_of_characters(more_than_max_length_input)
    registration_errors = RegistrationErrorLocators(page)
    expect(registration_errors.firstname_error_message).to_be_visible()
    expect(registration_errors.firstname_error_message).to_have_text(registration_firstname_error_message)








