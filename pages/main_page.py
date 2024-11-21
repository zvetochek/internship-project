from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MainPage(Page):

    # SETTINGS_BTN = (By.XPATH, "//div[text()='Settings']")
    # SETTINGS_BTN = (By.CSS_SELECTOR, "[href='/settings']")
    # SETTINGS_BTN = (By.CSS_SELECTOR, "[class*= 'menu_grid'] a[href*= 'settings']")
    SETTINGS_BTN = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
    MAIN_MENU_BTN_MOBILE = (By.CSS_SELECTOR, ".html-icon-bottom-bar.w-embed")
    PROFILE_BTN_MOBILE = (By.CSS_SELECTOR, ".menu-img-agent-listing")

    def click_settings_option(self):
        self.wait_and_click(*self.PROFILE_BTN_MOBILE)
        # self.wait_until_clickable(*self.SETTINGS_BTN)

    def click_main_menu_btn(self):
        self.wait_and_click(*self.MAIN_MENU_BTN_MOBILE)