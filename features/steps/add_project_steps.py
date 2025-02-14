from behave import given, when, then

@when('Add some test information to the input fields')
def add_test_information(context):
    context.app.add_project_page.add_test_information()

@then('Verify the right information is present in the input fields')
def verify_right_information_present(context):
    context.app.add_project_page.verify_right_information_present()

@then('Verify “Send an application” button is available and clickable')
def verify_send_application_btn(context):
    context.app.add_project_page.verify_send_application_btn()