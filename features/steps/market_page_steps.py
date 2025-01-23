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







