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

@when('Go to the final secondary page using the pagination button')
def go_to_final_secondary_page(context):
    context.app.secondary_page.go_to_final_secondary_page()

@when('Go back to the first secondary page using the pagination button')
def go_back_to_first_page(context):
    context.app.secondary_page.go_back_to_first_page()

@when('Filter the products by "want to sell"')
def filter_products_by_want_to_sell(context):
    context.app.secondary_page.filter_products_by_want_to_sell()

@when('Click on Apply Filter')
def click_apply_filter_btn(context):
    context.app.secondary_page.click_apply_filter_btn()

@then('Verify all cards have "for sale" tag')
def verify_all_cards_have_for_sale_tag(context):
    context.app.secondary_page.verify_all_cards_have_for_sale_tag()

@when('Filter the products by "want to buy"')
def filter_products_by_want_to_buy(context):
    context.app.secondary_page.filter_products_by_want_to_buy()

@then('Verify all cards have "want to buy" tag')
def verify_want_to_buy_tag(context):
    context.app.secondary_page.verify_want_to_buy_tag()