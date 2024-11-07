from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Reelly page')
def open_reelly(context):
    context.app.sign_in_page.open_reelly()
    context.driver.implicitly_wait(2)

@when('Enter email and password')
def input_email_and_password(context):
    context.app.sign_in_page.input_email_and_password()


@when('Click on Continue button')
def click_continue_btn(context):
    context.app.sign_in_page.click_continue_btn()


@when('Click on settings option')
def click_settings_option(context):
    context.app.main_page.click_settings_option()


@when('Click on Subscription & payments option')
def click_subcr_and_payment_btn(context):
    context.app.settings_page.click_subcr_and_payment_btn()


@then('Verify the right page opens')
def verify_subs_paym_url(context):
    context.app.subscrip_paym_page.verify_subs_paym_url()


@then('Verify title “Subscription & payments” is visible')
def verify_sp_title_visible(context):
    context.app.subscrip_paym_page.verify_sp_title_visible()


@then('Verify “back” and “upgrade plan” buttons are available')
def verify_buttons_displayed(context):
    context.app.subscrip_paym_page.verify_buttons_displayed()
