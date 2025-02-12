from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class SignInPage(Page):

    INPUT_EMAIL = (By.ID, "email-2")
    INPUT_PASSWORD = (By.ID, "field")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".login-button.w-button")
    #CONTINUE_BTN = (By.CSS_SELECTOR, "a.login-button[wized='loginButton']")
    # CONTINUE_BTN_MOBILE = (By.CSS_SELECTOR, '[wized="loginButton"]')
    PAGE_BODY = (By.CSS_SELECTOR, '.login-body')  # LOCATOR

    def open_reelly(self):
        self.open_url('https://soft.reelly.io')

    def login(self):
        self.input_text('larisale@gmail.com', *self.INPUT_EMAIL)
        self.input_text('utromrano', *self.INPUT_PASSWORD)
        self.click(*self.CONTINUE_BTN)


    # def click_continue_btn(self):
    #     self.driver.execute_script("window.scrollBy(0, 100)")
    #     self.click(*self.CONTINUE_BTN)

        #MOBILE TEST CODE FOR BROWSESTACK
    # def click_continue_btn(self):
    #     actions = ActionChains(self.driver)
    #     reely_page = self.find_element(*self.PAGE_BODY)
    #     actions.move_to_element(reely_page).click().perform()
    #     sleep(5)
    #     self.click(*self.CONTINUE_BTN_MOBILE)




