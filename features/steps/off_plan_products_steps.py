from behave import given, when, then

@when('Click on “off plan” at the left side menu')
def click_off_plan(context):
    context.app.off_plan_page.click_off_plan()

@then('Verify the right off-plan page opens')
def verify_off_plan_url(context):
    context.app.off_plan_page.verify_off_plan_url()

@when('Filter the products by price range from 1200000 to 2000000 AED')
def filter_products_by_price(context):
    context.app.off_plan_page.filter_products_by_price()

@then('Verify the price in all cards is in a given range')
def verify_price_in_range(context):
    context.app.off_plan_page.verify_price_in_range()

@when('Filter by sale status of “Out of Stocks”')
# def sales_status_out_of_stocks(context):
#     context.app.off_plan_page.sales_status_out_of_stocks()
def out_of_stock_tag(context):
    context.app.off_plan_page.out_of_stock_tag()

@then('Verify each product contains the Out of Stocks tag')
def verify_out_of_stock_tag(context):
    context.app.off_plan_page.verify_out_of_stock_tag()

@when('Click on the first product')
def click_first_product(context):
    context.app.off_plan_page.click_first_product()

@then('Verify the three options of visualization are “architecture”, “interior”, “lobby”')
def verify_opts_of_visualization(context):
    context.app.off_plan_page.verify_opts_of_visualization()

@then('Verify the visualization options are clickable')
def verify_visualiz_opts_clickable(context):
    context.app.off_plan_page.verify_visualiz_opts_clickable()