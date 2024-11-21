from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SettingsPage(Page):

    SUBSC_AND_PAYMENT_BTN = (By.XPATH, "//div[text()='Subscription & payments']")
    SUBSCRIPTION_BTN_MOBILE = (By.CSS_SELECTOR, "a[href='/subscription']")

    def click_subcr_and_payment_btn(self):
        # sleep(3)
        self.click(*self.SUBSC_AND_PAYMENT_BTN)
      # self.wait_and_click(*self.SUBSC_AND_PAYMENT_BTN)

    # def click_subcr_and_payment_btn(self):
    #     sleep(3)
    #     self.click(*self.SUBSCRIPTION_BTN_MOBILE)
