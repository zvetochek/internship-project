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

@when('Click on Edit profile option')
def click_edit_profile_option(context):
    context.app.settings_page.click_edit_profile_option()

@when('Change the language of the page to Russian. The option will be “RU” which is the list of the languages')
def change_language(context):
    context.app.settings_page.change_language()

@then('Verify the language has changed')
def verify_language_changed(context):
    context.app.settings_page.verify_language_changed()

@when('Click on "Add a project" button')
def click_add_project_option(context):
    context.app.settings_page.click_add_project_option()

@then('Verify the "Add a project" page opens')
def verify_add_project_page_opens(context):
    context.app.settings_page.verify_add_project_page_opens()

@when('Click on Community option')
def click_community_btn(context):
    context.app.settings_page.click_community_btn()

@when('Click on "Contact us" option')
def click_contact_us_option(context):
    context.app.settings_page.click_contact_us_option()

@when('Click on User Guide option')
def click_user_guide_option(context):
    context.app.settings_page.click_user_guide_option()
