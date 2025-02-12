from behave import given, when, then

@when('Click on “Secondary” option at the left side menu')
def click_secondary_menu(context):
    context.app.secondary_page.click_secondary_menu()

@then('Verify the secondary page opens')
def verify_secondary_page_opens(context):
    context.app.secondary_page.verify_secondary_page_opens()

@when('Click on Filters')
def click_filters_btn(context):
    context.app.secondary_page.click_filters_btn()

@when('Filter products by price range from 1200000 to 2000000 AED')
def filter_products_by_price(context):
    context.app.secondary_page.filter_products_by_price()

@then('Verify prices in all cards is in a given range')
def verify_price_in_range(context):
    context.app.secondary_page.verify_price_in_range()


