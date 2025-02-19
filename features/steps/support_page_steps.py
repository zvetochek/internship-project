from behave import given, when, then


@then('Verify the right page support opens')
def verify_support_page(context):
    context.app.support_page.verify_support_page()

@when('Go back')
def go_back_to_settings_page(context):
    context.app.support_page.go_back_to_settings_page()

