from behave import given, when, then

@then('Verify the User Guide page opens')
def verify_user_guide_page_opens(context):
    context.app.user_guide_page.verify_user_guide_page_opens()

@then('Verify all lesson videos contain titles')
def verify_videos_have_titles(context):
    context.app.user_guide_page.verify_videos_have_titles()