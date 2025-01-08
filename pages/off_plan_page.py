from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class OffPlanPage(Page):

    OFF_PLAN_BTN = (By.CSS_SELECTOR, "a[class='_1-link-menu w-inline-block w--current']")
    FILTER_BTN = (By.CSS_SELECTOR, "a[class='filter-button w-inline-block']")
    FROM_BOX_PRICE = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    TO_BOX_PRICE = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
    CARDS_PROPERTY = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
    OFF_PLAN_VALUE = (By.CSS_SELECTOR, "div[class='price-value']")

    def click_off_plan(self):
        self.click(*self.OFF_PLAN_BTN)

    def verify_off_plan_url(self):
        self.verify_url('https://soft.reelly.io/')

    def filter_products_by_price(self):
        self.click(*self.FILTER_BTN)
        self.input_text("1200000", *self.FROM_BOX_PRICE)
        self.input_text("2000000", *self.TO_BOX_PRICE)
        self.click(*self.APPLY_FILTER_BTN)


    def verify_price_in_range(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.CARDS_PROPERTY))
        for property in all_cards:
            property_price = property.find_element(*self.OFF_PLAN_VALUE)
            amount = property_price.text.replace('AED', '').replace(',', '')
            assert int(amount) in range(1200000, 2000000), f"Price not in Range"