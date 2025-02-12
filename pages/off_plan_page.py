from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class OffPlanPage(Page):

    OFF_PLAN_BTN = (By.CSS_SELECTOR, "a[class='_1-link-menu w-inline-block w--current']")
    FILTER_BTN = (By.CSS_SELECTOR, "a[class='filter-button w-inline-block']")
    FROM_BOX_PRICE = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    TO_BOX_PRICE = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
    CARDS_PROPERTY = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
    OFF_PLAN_VALUE = (By.CSS_SELECTOR, "div[class='price-value']")
    SALE_STATUS_DROPDOWN = (By.CSS_SELECTOR, "#Location-2")
    OUT_OF_STOCK_DROPDOWN = (By.CSS_SELECTOR, "option[value='Out of stock']")
    OUT_OF_STOCK_CARDS = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
    OUT_OT_STOCK_STATUS_ON_CARDS = (By.CSS_SELECTOR, "div[wized='projectStatus'")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
    OFF_PLAN_CARD_IMAGE = (By.CSS_SELECTOR, "div[wized='projectImage']")
    OFF_PLAN_CARD_TITLE = (By.CSS_SELECTOR, "div[wized='projectName']")
    NEXT_PAGE_BTN_OFF_PLAN = (By.CSS_SELECTOR, "a[wized='nextPageProperties']")
    PREVIOUS_PAGE_BTN_OFF_PLAN = (By.CSS_SELECTOR, "div[wized='previousPageProperties']")
    TOTAL_PAGE = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')

    ARCHITECTURE_BTN = (By.ID, 'w-tabs-0-data-w-tab-0')
    INTERIOR_BTN = (By.ID, 'w-tabs-0-data-w-tab-1')
    LOBBY_BTN = (By.ID, 'w-tabs-0-data-w-tab-2')


    def __init__(self, driver):
        super().__init__(driver)
        self.SALES_STATUS_DROPDOWN = None

    def click_off_plan(self):
        self.click(*self.OFF_PLAN_BTN)

    def verify_off_plan_url(self):
        self.verify_url('https://soft.reelly.io/')

    def filter_products_by_price(self):
        self.wait_and_click(*self.FILTER_BTN)
        self.input_text("1200000", *self.FROM_BOX_PRICE)
        self.input_text("2000000", *self.TO_BOX_PRICE)
        self.wait_and_click(*self.APPLY_FILTER_BTN)

    def verify_price_in_range(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.CARDS_PROPERTY))
        for property in all_cards:
            property_price = property.find_element(*self.OFF_PLAN_VALUE)
            amount = property_price.text.replace('AED', '').replace(',', '')
            assert int(amount) in range(1200000, 2000000), f"Price not in Range"

    def out_of_stock_tag(self):
        # self.select_dropdown_value('Out of stock', *self.SALE_STATUS_DD)
        dd = self.find_element(*self.SALE_STATUS_DROPDOWN)
        select = Select(dd)
        select.select_by_value('Out of stock')
        sleep(3)

    def verify_out_of_stock_tag(self):
        all_cards = self.find_elements(*self.OUT_OF_STOCK_CARDS)
        for card in all_cards:
            status = card.find_element(*self.OUT_OT_STOCK_STATUS_ON_CARDS)
            assert status.text == "Out of stock", f"Tag is not 'Out of stock'."

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT)

    def verify_opts_of_visualization(self):
        self.verify_text('Architecture', *self.ARCHITECTURE_BTN)
        self.verify_text('Interior', *self.INTERIOR_BTN)
        self.verify_text('Lobby', *self.LOBBY_BTN)

    def verify_visualiz_opts_clickable(self):
        self.wait_until_clickable_click(*self.ARCHITECTURE_BTN)
        self.wait_until_clickable_click(*self.INTERIOR_BTN)
        self.wait_until_clickable_click(*self.LOBBY_BTN)

    def verify_products_have_title_n_picture(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.CARDS_PROPERTY))
        for card in all_cards:
            title = self.find_elements(*self.OFF_PLAN_CARD_TITLE)
            picture = self.find_elements(*self.OFF_PLAN_CARD_IMAGE)

            if not picture or not title:
                print(f"Missing picture or title for card: {card}")

        print(len(all_cards))

        # all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.CARDS_PROPERTY))
        # for card in all_cards:
        #     title = self.find_elements(*self.OFF_PLAN_CARD_TITLE)
        #     assert len(title) == len(all_cards), f'Expected {len(all_cards)}, got {len(title)}'
        #     picture = self.find_elements(*self.OFF_PLAN_CARD_IMAGE)
        #     assert len(picture) == len(all_cards), f'Expected {len(all_cards)}, got {len(picture)}'
        #
        # print(len(all_cards))

    def goto_final_page_using_pagination_offplan(self):
        sleep(5)
        total_page = self.find_element(*self.TOTAL_PAGE).text
        for page in range(1, int(total_page)):
            #self.find_elements(*self.NEXT_PAGE_BTN_OFF_PLAN)
            # sleep(1)
            self.wait_and_click(*self.NEXT_PAGE_BTN_OFF_PLAN)
            print(f"Current page: {page}") #Print each page number

    def goback_to_first_page_using_pagination(self):
        sleep(5)
        total_page = self.find_element(*self.TOTAL_PAGE).text
        for page in range(int(total_page), 0, -1):
           # self.find_elements(*self.PREVIOUS_PAGE_BTN_OFF_PLAN)
            self.wait_and_click(*self.PREVIOUS_PAGE_BTN_OFF_PLAN)
            print(f"Current {page}") #Print each page number






