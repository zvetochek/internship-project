from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@then('Verify the verification page opens')
def verify_verification_page_opened(context):
    context.app.verification_page.verify_verification_page_opened()


@then('Verify “upload image” and “Next step” buttons are available')
def verify_uploadimg_nextstep_btns(context):
    context.app.verification_page.verify_uploadimg_nextstep_btns()
