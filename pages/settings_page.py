from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SettingsPage(Page):

    SUBSC_AND_PAYMENT_BTN = (By.XPATH, "//div[text()='Subscription & payments']")
    SUBSCRIPTION_BTN_MOBILE = (By.CSS_SELECTOR, "a[href='/subscription']")
    VERIFICATION_OPTION = (By.CSS_SELECTOR, "a[href='/verification/step-0']")
    CONNECT_THE_COMPANY_BTN = (By.XPATH, "//div[@class='get-free-period menu' and text()='Connect the company']")
    # CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, "div[class='settings-block-menu'] div[class='get-free-period menu']")
    # this locator works as well!
    EDIT_PROFILE_BTN = (By.CSS_SELECTOR, "[href*='profile-edit']")
    # EDIT_PROFILE_BTN = By.XPATH, "//div[contains(@class, 'setting-text') and text()='Edit profile']")
    # this locator works as well!


    def click_subcr_and_payment_btn(self):
        # sleep(3)
        self.click(*self.SUBSC_AND_PAYMENT_BTN)
      # self.wait_and_click(*self.SUBSC_AND_PAYMENT_BTN)

    # def click_subcr_and_payment_btn(self):
    #     sleep(3)
    #     self.click(*self.SUBSCRIPTION_BTN_MOBILE)

    def click_verification_option(self):
        self.click(*self.VERIFICATION_OPTION)

    def click_connect_company_btn(self):
        self.wait_and_click(*self.CONNECT_THE_COMPANY_BTN)

    def switch_tab(self):
        self.switch_to_new_window()

    def verify_right_tab_opens(self):
        self.verify_url('https://soft.reelly.io/payment/personal')

    def click_edit_profile_option(self):
        self.wait_and_click(*self.EDIT_PROFILE_BTN)