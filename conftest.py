import pytest
from playwright.sync_api import Page, expect
# from variables import *
from constants.urls import *
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

@pytest.fixture
def go_to_register_page(page: Page):
    page.goto(base_url)
    home_page = HomePage(page)
    home_page.click_my_account_dropdown()
    home_page.click_register_button()
    register_page = RegisterPage(page)
    expect(page).to_have_url(registration_page_url)
    assert register_page.register_page_title.inner_text() == "Register Account"
    return register_page


@pytest.fixture
def go_to_login_page(page: Page):
    page.goto(base_url)
    home_page = HomePage(page)
    home_page.click_my_account_dropdown()
    home_page.click_login_button()
    expect(page).to_have_url(login_url)
    login_page = LoginPage(page)
    return login_page