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
    NEXT_PAGE = (By.CSS_SELECTOR, "[class='pagination__button w-inline-block']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "[class='pagination__button']")
    TOTAL_PAGE_SEC = (By.CSS_SELECTOR, "[wized='totalPageProperties']")
    CURRENT_PAGE = (By.CSS_SELECTOR, "[wized='currentPageProperties']")
    PAGINATION = (By.CSS_SELECTOR, ".pagination-text")
    WANT_TO_SELL_BTN = (By.CSS_SELECTOR, "div[wized='ListingTypeSell']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButtonMLS']")
    FOR_SALE_TAG = (By.CSS_SELECTOR, "div[class='for-sale-tag']")
    WANT_TO_BUY_BTN = (By.XPATH, "//div[contains(@class, 'tag-text-filters') and text()='Want to buy']")
    LISTING_CARDS_WANT_TO_BUY = (By.CSS_SELECTOR, "div[wized='listingCardMLS']")
    WANT_TO_BUY_TAG = (By.CSS_SELECTOR, "div.for-sale-tag")

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

    def go_to_final_secondary_page(self):
        sleep(5)
        total_page = self.find_element(*self.TOTAL_PAGE_SEC).text
        for page in range(1, int(total_page)):
            self.wait_and_click(*self.NEXT_PAGE)
            print(f"Current page: {page}")  # Print each page number

    def go_back_to_first_page(self):
        sleep(5)
        total_page = self.find_element(*self.TOTAL_PAGE_SEC).text
        for page in range(int(total_page), 0, -1):
            # self.find_elements(*self.PREVIOUS_PAGE_BTN_OFF_PLAN)
            self.wait_and_click(*self.PREVIOUS_PAGE)
            print(f"Current {page}")  # Print each page number


    def filter_products_by_want_to_sell(self):
        self.wait_and_click(*self.WANT_TO_SELL_BTN)

    def click_apply_filter_btn(self):
        self.wait_and_click(*self.APPLY_FILTER_BTN)

    def verify_for_sale_tag(self):
        for_sale_cards = self.find_elements(*self.LISTING_CARDS)
        for_sale_tags = self.find_elements(*self.FOR_SALE_TAG)
        assert len(for_sale_tags) == len(for_sale_cards), f"Expected {len(for_sale_cards)}, got {len(for_sale_tags)}"

    def verify_all_cards_have_for_sale_tag(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.LISTING_CARDS))
        for card in all_cards:
            tag = card.find_element(*self.FOR_SALE_TAG).text
            assert 'for sale' in tag.lower(), f"Tag does not contain 'for sale' in card: {card}"

    def filter_products_by_want_to_buy(self):
        self.wait_and_click(*self.WANT_TO_BUY_BTN)

    def verify_want_to_buy_tag(self):
        listing_cards = self.find_elements(*self.LISTING_CARDS_WANT_TO_BUY)
        want_to_buy_tags = self.find_elements(*self.WANT_TO_BUY_TAG)
        assert len(want_to_buy_tags) == len(listing_cards), f"Expected {len(listing_cards)}, got {len(want_to_buy_tags)}"
