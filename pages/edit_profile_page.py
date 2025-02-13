from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class EditProfilePage(Page):

    TEST_NAME = (By.ID, "Fullname")
    TEST_PHONE_NUMBER = (By.ID, "number")
    TEST_EMAIL = (By.ID, "Email-2")
    SOCIAL_MEDIA = (By.ID, "Email")
    CLOSE_PROFILE_BTN = (By.CSS_SELECTOR, "[class='close-button w-button']")
    SAVE_CHANGES_PROFILE_BTN = (By.CSS_SELECTOR, ".profile-button-block .save-changes-button")

    def enter_info_to_input_fields(self):
        sleep(2)
        self.clear_text(*self.TEST_NAME)
        sleep(3)
        self.input_text("Lu", *self.TEST_NAME)
        self.clear_text(*self.TEST_PHONE_NUMBER)
        self.input_text("1112223334", *self.TEST_PHONE_NUMBER)
        self.clear_text(*self.TEST_EMAIL)
        self.input_text("data@test.com", *self.TEST_EMAIL)
        self.clear_text(*self.SOCIAL_MEDIA)
        self.input_text("https://www.careerist.com", *self.SOCIAL_MEDIA)
        # social_icons_names = ['Instagram', 'Telegram', 'Youtube', 'Facebook', 'Twitter', 'TikTok', 'Pinterest', 'Snapchat','LinkedIn']

    def check_right_info_present_in_fields(self):
        # sleep(3)
        self.verify_attribute_value("Lu", *self.TEST_NAME)
        self.verify_attribute_value("1112223334", *self.TEST_PHONE_NUMBER)
        self.verify_attribute_value("data@test.com", *self.TEST_EMAIL)
        self.verify_attribute_value("https://www.careerist.com", *self.SOCIAL_MEDIA)

    def check_close_and_savechanges_btns_clickable(self):
    # self.verify_text('Close', *self.CLOSE_PROFILE_BTN)
    # self.verify_text('Save changes', *self.SAVE_CHANGES_PROFILE_BTN)
        self.presence_of_element_located(*self.CLOSE_PROFILE_BTN)
        self.wait_until_clickable(*self.CLOSE_PROFILE_BTN)
        self.presence_of_element_located(*self.SAVE_CHANGES_PROFILE_BTN)
        self.wait_until_clickable(*self.SAVE_CHANGES_PROFILE_BTN)