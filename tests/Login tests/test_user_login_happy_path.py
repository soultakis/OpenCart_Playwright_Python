from playwright.sync_api import Page, expect
from variables import *
from conftest import go_to_login_page
from pages.user_homepage import UserHomePage


def test_login_happy_path(page:Page, go_to_login_page):
    login_page = go_to_login_page
    login_page.login_success()
    user_homepage = UserHomePage(page)
    list_texts = user_homepage.verify_user_logged_in()
    for i in range(len(list_texts)):
        assert list_texts[i] == user_logged_in_titles[i]



