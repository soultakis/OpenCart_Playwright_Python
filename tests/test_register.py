from playwright.sync_api import Page, expect
from conftest import go_to_register_page
from pages.registration_error_locators import RegistrationErrorLocators
from variables import *
from pages.registration_error_locators import RegistrationErrorLocators
from pages.home_page import HomePage
from pages.register_page import RegisterPage


# def test_goto_register_page(page: Page, go_to_register_page):
#     register_page = go_to_register_page
#     expect(register_page.register_page_title).to_be_visible()
#     assert register_page.register_page_title.inner_text() == "Register Account"


def test_register_success_no_subscribe(page: Page, go_to_register_page):
    register_page = go_to_register_page

    success_message, success_title = register_page.register_success_no_subscribe()
    assert success_title.inner_text() == registration_success_title
    for i in range(len(success_message)):
        assert success_message[i].inner_text() == registration_success_messages[i]


def test_register_success_yes_subscription(page: Page, go_to_register_page):
    register_page = go_to_register_page

    success_message, success_title = register_page.register_success_yes_subscribe()
    assert page.url == registration_success_url
    assert success_title.inner_text() == registration_success_title
    for i in range(len(success_message)):
        assert success_message[i].inner_text() == registration_success_messages[i]

def test_register_empty_form(page: Page, go_to_register_page):
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

def test_validate_empty_fields(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.fill_all_fields()
    register_page.accept_terms.check()

