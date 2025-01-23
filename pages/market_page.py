from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep


class MarketPage(Page):

    MARKET_BTN = (By.CSS_SELECTOR, "a[href='/market-companies']")
    NEXT_PAGE_BTN = (By.CSS_SELECTOR, "a[wized='nextPageMarket']")
    BACK_PAGE_BTN = (By.CSS_SELECTOR, "div[wized='previousPageMarket']")
    DEVELOPERS_BTN = (By.CSS_SELECTOR, "div[wized='marketTagDevelopers']")
    MARKET_CARDS_IMAGE = (By.CSS_SELECTOR, "img[wized='marketPageBackgraundPhoto']")
    LICENSE_TAG = (By.CSS_SELECTOR, "div[class='license-block']")


    def click_market_menu(self):
        self.click(*self.MARKET_BTN)

    def verify_market_page(self):
        self.verify_url('https://soft.reelly.io/market-companies')

    def go_to_final_market_page(self):
        # self.driver.execute_script("window.scrollBy(0,2000)", "")
        # sleep(4)
        # self.driver.execute_script("window.scrollBy(0,2000)", "")

        for page in range(1, 9):
            self.find_elements(*self.NEXT_PAGE_BTN)
            sleep(1)
            self.wait_and_click(*self.NEXT_PAGE_BTN)
            print(f"Current page: {page}") #Print each page number

    def go_to_first_page(self):
        # self.driver.execute_script("window.scrollBy(0,2000)", "")
        # sleep(4)
        # self.driver.execute_script("window.scrollBy(0,2000)", "")

        for page in range(8, 0, -1):
            self.find_elements(*self.BACK_PAGE_BTN)
            # sleep(1)
            self.wait_and_click(*self.BACK_PAGE_BTN)
            print(f"Current {page}")  #Print each page number


    def click_developers_filter(self):
        self.click(*self.DEVELOPERS_BTN)

    def verify_cards_have_license_tag(self):
        self.wait_for_all_visibility_elements_located(*self.MARKET_CARDS_IMAGE)
        all_cards = self.find_elements(*self.LICENSE_TAG)
        # print(len(all_cards))
        print(f"Total number of cards: {len(all_cards)}")

        for card in all_cards:
            assert 'License' in card.text, f"No License tag in card."


