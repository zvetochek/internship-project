from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class VerificationPage(Page):
    UPLOAD_IMAGE_BTN = (By.CSS_SELECTOR, "div.upload-button-2")
    NEXT_STEP_BTN = (By.CSS_SELECTOR, "div[class='next-step--']")

    def verify_verification_page_opened(self):
        self.verify_url('https://soft.reelly.io/verification/step-0')


    def verify_uploadimg_nextstep_btns(self):
        self.wait_for_element_appear(*self.UPLOAD_IMAGE_BTN)
        self.wait_for_element_appear(*self.NEXT_STEP_BTN)

        # self.wait_for_visibility_of_element_located(*self.UPLOAD_IMAGE_BTN)
        # self.wait_for_visibility_of_element_located(*self.NEXT_STEP_BTN)



