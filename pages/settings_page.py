from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsPage(Page):

    SUBSC_AND_PAYMENT_BTN = (By.XPATH, "//div[text()='Subscription & payments']")


    def click_subcr_and_payment_btn(self):
      self.click(*self.SUBSC_AND_PAYMENT_BTN)