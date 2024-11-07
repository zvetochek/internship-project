from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):

    INPUT_EMAIL = (By.ID, "email-2")
    INPUT_PASSWORD = (By.ID, "field")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".login-button.w-button")


    def open_reelly(self):
        self.open_url('https://soft.reelly.io')

    def input_email_and_password(self):
        # sleep(5)
        self.input_text('larisale@gmail.com', *self.INPUT_EMAIL)
        self.input_text('utromrano', *self.INPUT_PASSWORD)

    def click_continue_btn(self):
        self.click(*self.CONTINUE_BTN)



