from playwright.sync_api import expect
from variables import *
from conftest import go_to_login_page

def test_login_empty_email_and_password(go_to_login_page):
    login_page = go_to_login_page
    login_page.login_procedure("", "")
    expect(login_page.invalid_login_warning).to_have_text(login_invalid_credentials_error_message)

def test_login_empty_email(go_to_login_page):
    login_page = go_to_login_page
    login_page.login_procedure("", valid_password)
    expect(login_page.invalid_login_warning).to_have_text(login_invalid_credentials_error_message)

def test_login_empty_password(go_to_login_page):
    login_page = go_to_login_page
    login_page.login_procedure(valid_email, "")
    expect(login_page.invalid_login_warning).to_have_text(login_invalid_credentials_error_message)

def test_login_invalid_email(go_to_login_page):
    login_page = go_to_login_page
    login_page.login_procedure(invalid_email, valid_password)
    expect(login_page.invalid_login_warning).to_have_text(login_invalid_credentials_error_message)

def test_login_invalid_password(go_to_login_page):
    login_page = go_to_login_page
    login_page.login_procedure(valid_email, invalid_password)
    expect(login_page.invalid_login_warning).to_have_text(login_invalid_credentials_error_message)