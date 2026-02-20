from playwright.sync_api import Page, expect
from constants.login_page_constants import *
from conftest import go_to_login_page

def test_verify_login_page_right_side_menu_items(page: Page, go_to_login_page):
    login_page = go_to_login_page
    for i in range(len(login_page.right_side_menu_items.all())):
        expect(login_page.right_side_menu_items.all()[i]).to_be_visible()
        expect(login_page.right_side_menu_items.all()[i]).to_have_text(login_page_right_side_menu[i])

