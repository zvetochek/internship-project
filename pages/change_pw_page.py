from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class ChangePwPage(Page):

    ENTER_NEW_PW = (By.CSS_SELECTOR, "#Enter-new-password")
    REPEAT_PW = (By.CSS_SELECTOR, "#Repeat-password")
    CHANGE_PW_BTN = (By.CSS_SELECTOR, "a[wized*='changePasswordButton']")

    def verify_change_pw_page(self):
        self.verify_url('https://soft.reelly.io/set-new-password')


    def add_test_pw(self):
        self.input_text('changepw',*self.ENTER_NEW_PW)
        self.input_text("changepw",*self.REPEAT_PW)


    def verify_change_pw_btn(self):
        self.presence_of_element_located(*self.CHANGE_PW_BTN)
