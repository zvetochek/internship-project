from behave import given, when, then

@then('Verify the Community page opens')
def verify_community_page_opens(context):
    context.app.community_page.verify_community_page_opens()

@then('Verify “Contact support” button is available and clickable')
def verify_contact_support_btn(context):
    context.app.community_page.verify_contact_support_btn()
