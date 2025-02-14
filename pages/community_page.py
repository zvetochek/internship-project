from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class CommunityPage(Page):

    SUPPORT_BTN = (By.CSS_SELECTOR, ".support-fixed-button.w-inline-block")

    def verify_community_page_opens(self):
       self.verify_partial_url('community')

    def  verify_contact_support_btn(self):
        self.presence_of_element_located(*self.SUPPORT_BTN)
        self.wait_until_clickable(*self.SUPPORT_BTN)



