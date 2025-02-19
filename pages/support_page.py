from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class SupportPage(Page):

    def verify_support_page(self):
        self.verify_partial_url("api.whatsapp.com")

    def go_back_to_settings_page(self):
        # self.driver.close()
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[0])



