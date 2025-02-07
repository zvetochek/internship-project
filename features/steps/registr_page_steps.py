from behave import given, when, then
from time import sleep

@given('Open the registration or sign up page')
def open_registr_page(context):
    context.app.registr_page.open_registr_page()

@when('Enter some test information in the input fields')
def enter_registr_info(context):
    context.app.registr_page.enter_registr_info()


@then('Verify the right information is present')
def verify_registr_info(context):
    context.app.registr_page.verify_registr_info()
