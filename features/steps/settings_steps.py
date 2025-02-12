from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Click on the verification option')
def click_verification_option(context):
    context.app.settings_page.click_verification_option()

@when('Click on “Connect the company”')
def click_connect_company_btn(context):
    context.app.settings_page.click_connect_company_btn()

@when('Switch the new tab')
def switch_to_new_tab(context):
    context.app.settings_page.switch_tab()

@then('Verify the right tab opens')
def verify_right_tab_opens(context):
    context.app.settings_page.verify_right_tab_opens()