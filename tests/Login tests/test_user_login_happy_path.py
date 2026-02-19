from playwright.sync_api import Page, expect
from variables import *
from conftest import go_to_login_page
from pages.my_account import MyAccount


def test_login_happy_path(page:Page, go_to_login_page):
    login_page = go_to_login_page
    login_page.login_procedure(valid_email, valid_password)
    user_homepage = MyAccount(page)
    list_texts = user_homepage.read_successful_logged_in_messages()
    for i in range(len(list_texts)):
        expect(list_texts[i]).to_have_text(user_logged_in_titles[i])