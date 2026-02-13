from playwright.sync_api import Page, expect
from conftest import go_to_register_page
from variables import *


def test_register_success_no_subscribe(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.submit_registration_form(subscribe=False)
    expect(page).to_have_url(registration_success_url)
    expect(register_page.successful_title).to_have_text(registration_success_title)
    for i in range(len(register_page.success_message.all())):
        expect(register_page.success_message.all()[i]).to_have_text(registration_success_messages[i])



def test_register_success_yes_subscription(page: Page, go_to_register_page):
    register_page = go_to_register_page
    register_page.submit_registration_form(subscribe=True)
    expect(page).to_have_url(registration_success_url)
    expect(register_page.successful_title).to_have_text(registration_success_title)
    for i in range(len(register_page.success_message.all())):
        expect(register_page.success_message.all()[i]).to_have_text(registration_success_messages[i])




