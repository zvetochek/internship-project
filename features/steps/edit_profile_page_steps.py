from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Enter test information in the input fields')
def enter_info_to_input_fields(context):
    context.app.edit_profile_page.enter_info_to_input_fields()

@then('Check the right information is present in the input fields')
def check_right_info_present_in_fields(context):
    context.app.edit_profile_page.check_right_info_present_in_fields()

@then('Check “Close” and “Save Changes” buttons are available and clickable')
def check_close_and_savechanges_btns_clickable(context):
    context.app.edit_profile_page.check_close_and_savechanges_btns_clickable()
