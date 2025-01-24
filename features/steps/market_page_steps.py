from behave import given, when, then

@when('Click on “market” at the left side menu')
def click_market_menu(context):
    context.app.market_page.click_market_menu()

@then('Verify the Market page opens')
def verify_market_page(context):
    context.app.market_page.verify_market_page()

@when('Go to the final page using pagination')
def go_to_final_market_page(context):
    context.app.market_page.go_to_final_market_page()

@when('Go to the first page using pagination')
def go_to_first_page(context):
    context.app.market_page.go_to_first_page()

@when('Click on Developers filter at the top of the page')
def click_developers_filter(context):
    context.app.market_page.click_developers_filter()

@then('Verify all cards have the license tag')
def verify_cards_have_license_tag(context):
    context.app.market_page.verify_cards_have_license_tag()

@when('Click on “Add company” button')
def add_company_button(context):
    context.app.market_page.add_company_button()

@then('Verify the "Add company" page opens')
def verify_add_company_page_opened(context):
    context.app.market_page.verify_add_company_page_opened()

@then('Verify the button “Publish my company” is available')
def verify_publish_my_company_btn_available(context):
    context.app.market_page.verify_publish_my_company_btn_available()









