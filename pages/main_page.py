from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    SETTING_BTN = (By.XPATH, "//div[text()='Settings']")

    def click_settings_option(self):
        self.wait_and_click(*self.SETTING_BTN)

