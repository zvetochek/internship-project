from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open Reelly page')
def open_reelly(context):
    context.app.sign_in_page.open_reelly()
    context.driver.implicitly_wait(4)

@when('Enter email and password')
def input_email_and_password(context):
    sleep(3)
    context.app.sign_in_page.input_email_and_password()


@when('Click on Continue button')
def click_continue_btn(context):
    sleep(5)
    context.app.sign_in_page.click_continue_btn()
    # context.driver.find_element(By.CSS_SELECTOR......) # IF I work without 'pages'


@when('Click on Main Menu')
def click_main_menu_btn(context):
    context.app.main_page.click_main_menu_btn()


@when('Click on profile icon')
def click_settings_option(context):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(3)
    context.app.main_page.click_settings_option()


@when('Click on Subscription & payments option')
def click_subcr_and_payment_btn(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.settings_page.click_subcr_and_payment_btn()
    # sleep(5)

@then('Verify the right page opens')
def verify_subs_paym_url(context):
    context.app.subscrip_paym_page.verify_subs_paym_url()


@then('Verify title “Subscription & payments” is visible')
def verify_sp_title_visible(context):
    context.app.subscrip_paym_page.verify_sp_title_visible()


@then('Verify “back” and “upgrade plan” buttons are available')
def verify_buttons_displayed(context):
    context.app.subscrip_paym_page.verify_buttons_displayed()
