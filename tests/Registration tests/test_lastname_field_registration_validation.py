from playwright.sync_api import Page, expect
from conftest import go_to_register_page
from variables import *
from pages.registration_error_locators import RegistrationErrorLocators


def test_empty_lastname_validation(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_lastname_validation()
    register_page.click_continue()
    registration_errors = RegistrationErrorLocators(page)
    expect(registration_errors.lastname_error_message).to_have_text(registration_lastname_error_message)


def test_validate_lastname_minimum_length(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_lastname_validation()
    register_page.enter_lastname_number_of_characters(min_name_length_input)
    expect(register_page.successful_title).to_have_text(registration_success_title)
    for i in range(len(register_page.success_message.all())):
        expect(register_page.success_message.all()[i]).to_have_text(registration_success_messages[i])

def test_validate_lastname_maximum_length(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_lastname_validation()
    register_page.enter_lastname_number_of_characters(max_name_length_input)
    expect(register_page.successful_title).to_have_text(registration_success_title)
    for i in range(len(register_page.success_message.all())):
        expect(register_page.success_message.all()[i]).to_have_text(registration_success_messages[i])

def test_validate_lastname_length_more_than_maximum(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.prepare_lastname_validation()
    register_page.enter_lastname_number_of_characters(more_than_max_name_length_input)
    registration_errors = RegistrationErrorLocators(page)
    expect(registration_errors.lastname_error_message).to_be_visible()
    expect(registration_errors.lastname_error_message).to_have_text(registration_lastname_error_message)








