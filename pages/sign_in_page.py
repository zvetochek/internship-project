from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SignInPage(Page):

    INPUT_EMAIL = (By.ID, "email-2")
    INPUT_PASSWORD = (By.ID, "field")
    # CONTINUE_BTN = (By.CSS_SELECTOR, ".login-button.w-button")
    #CONTINUE_BTN = (By.CSS_SELECTOR, "a.login-button[wized='loginButton']")
    CONTINUE_BTN_MOBILE = (By.CSS_SELECTOR, '[wized="loginButton"]')
    def open_reelly(self):
        self.open_url('https://soft.reelly.io')

    def input_email_and_password(self):
        self.input_text('larisale@gmail.com', *self.INPUT_EMAIL)
        self.input_text('utromrano', *self.INPUT_PASSWORD)


    def click_continue_btn(self):
        #self.click(*self.CONTINUE_BTN)

        #MOBILE TEST CODE FOR BROWSESTACK
        self.driver.execute_script("window.scrollBy(0, 100)")
        sleep(5)
        self.click(*self.CONTINUE_BTN_MOBILE)




