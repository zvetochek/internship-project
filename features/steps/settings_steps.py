from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Click on the verification option')
def click_verification_option(context):
    context.app.settings_page.click_verification_option()