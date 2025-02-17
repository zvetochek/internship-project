from behave import given, when, then

@then('Verify Change password page opens')
def verify_change_pw_page(context):
    context.app.change_pw_page.verify_change_pw_page()

@when('Add some test password to the input fields')
def add_test_pw(context):
    context.app.change_pw_page.add_test_pw()

@then('Verify the “Change password” button is available, but don’t click on it')
def verify_change_pw_btn(context):
    context.app.change_pw_page.verify_change_pw_btn()
