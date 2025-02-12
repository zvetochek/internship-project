from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class SecondaryPage(Page):

    # SECONDARY_BTN = (By. XPATH, "//div[@class='menu-button-text' and text()='Secondary']")
    SECONDARY_BTN = (By.CSS_SELECTOR, "a[href='/secondary-listings'].menu-button-block")
    SECONDARY_FILTER_BTN = (By.CSS_SELECTOR, "div[class='filter-button']")
    # SECONDARY_FILTER_BTN = (By.CSS_SELECTOR, "a[class='filter-button w-inline-block']")
    FROM_BOX_PRICE_SECONDARY = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    TO_BOX_PRICE_SECONDARY = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_FILTER_BTN_SECONDARY = (By.CSS_SELECTOR, "a[wized='applyFilterButtonMLS']")
    LISTING_CARDS = (By.CSS_SELECTOR, "div[class='listing-card']")
    SECONDARY_CARD_PRICE = (By.CSS_SELECTOR, "div[wized='unitPriceMLS']")


    def click_secondary_menu(self):
        sleep(4)
        self.wait_and_click(*self.SECONDARY_BTN)

    def verify_secondary_page_opens(self):
        self.verify_url('https://soft.reelly.io/secondary-listings')

    def click_filters_btn(self):
        sleep(2)
        self.wait_and_click(*self.SECONDARY_FILTER_BTN)

    def filter_products_by_price(self):
        # sleep(5)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        self.input_text("1200000", *self.FROM_BOX_PRICE_SECONDARY)
        # sleep(1)
        self.input_text("2000000", *self.TO_BOX_PRICE_SECONDARY)
        # sleep(2)
        self.wait_and_click(*self.APPLY_FILTER_BTN_SECONDARY)

    def verify_price_in_range(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.LISTING_CARDS))
        for property in all_cards:
            property_price = property.find_element(*self.SECONDARY_CARD_PRICE)
            amount = property_price.text.replace('AED', '').replace(',', '')
            assert int(amount) in range(1200000, 2000000), f"Price not in Range"

