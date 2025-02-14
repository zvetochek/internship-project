from behave import given, when, then

@then('Verify the "Contact us" page opens')
def verify_contact_us_page_opens(context):
    context.app.contact_us_page.verify_contact_us_page_opens()

@then('Verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    context.app.contact_us_page.verify_social_media_icons()

@then('Verify “Connect the company” button is available and clickable')
def verify_connect_the_company_btn_avlbl_clickable(context):
    context.app.contact_us_page.verify_connect_the_company_btn()