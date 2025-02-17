from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class SettingsPage(Page):

    SUBSC_AND_PAYMENT_BTN = (By.XPATH, "//div[text()='Subscription & payments']")
    SUBSCRIPTION_BTN_MOBILE = (By.CSS_SELECTOR, "a[href='/subscription']")
    VERIFICATION_OPTION = (By.CSS_SELECTOR, "a[href='/verification/step-0']")
    CONNECT_THE_COMPANY_BTN = (By.XPATH, "//div[@class='get-free-period menu' and text()='Connect the company']")
    # CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, "div[class='settings-block-menu'] div[class='get-free-period menu']")
    # this locator works as well!
    EDIT_PROFILE_BTN = (By.CSS_SELECTOR, "[href*='profile-edit']")
    # EDIT_PROFILE_BTN = By.XPATH, "//div[contains(@class, 'setting-text') and text()='Edit profile']")
    # this locator works as well!
    # CHANGE_LANGUAGE = (By.CSS_SELECTOR, "[class='wg-dd-1-togle-3 w-dropdown-toggle']")
    LANGUAGE_SELECTOR = (By.ID, "w-dropdown-toggle-0")
    RU_LANGUAGE = (By.ID, "w-dropdown-list-0")
    RUSSIAN_HEADER = (By.CSS_SELECTOR, "div[class='div-block-33']")
    ADD_PROJECT_BTN = (By.XPATH, "//*[text()='Add a project']")
    # ADD_PROJECT_BTN = (By.CSS_SELECTOR, "[href*='add-a-project'].page-setting-block")
    # this locator works as well
    COMMUNITY_BTN = (By.CSS_SELECTOR, "[href*='community'].page-setting-block")
    CONTACT_US_BTN = (By.CSS_SELECTOR, "[href*='/contact-us'].page-setting-block")
    USER_GUIDE_BTN = (By.CSS_SELECTOR, "a[href*='/user-guide'].page-setting-block")
    CHANGE_PW_BTN = (By.CSS_SELECTOR, "a[href*='/set-new-password']")


    def click_subcr_and_payment_btn(self):
        # sleep(3)
        self.click(*self.SUBSC_AND_PAYMENT_BTN)
      # self.wait_and_click(*self.SUBSC_AND_PAYMENT_BTN)

    # def click_subcr_and_payment_btn(self):
    #     sleep(3)
    #     self.click(*self.SUBSCRIPTION_BTN_MOBILE)

    def click_verification_option(self):
        self.click(*self.VERIFICATION_OPTION)

    def click_connect_company_btn(self):
        self.wait_and_click(*self.CONNECT_THE_COMPANY_BTN)

    def switch_tab(self):
        self.switch_to_new_window()

    def verify_right_tab_opens(self):
        self.verify_url('https://soft.reelly.io/payment/personal')

    def click_edit_profile_option(self):
        self.wait_and_click(*self.EDIT_PROFILE_BTN)

    def change_language(self):
        # self.wait_until_visible(*self.LANGUAGE_SELECTOR)
        # actions = ActionChains(self.driver)
        # language = self.find_element(*self.LANGUAGE_SELECTOR)
        # # move to the element and click then perform the operation
        # actions.move_to_element(language)
        # element = self.find_element(*self.RU_LANGUAGE)
        # actions.move_to_element(element)
        # # actions.move_by_offset(0, 25)
        # sleep(2)
        # actions.click()
        # actions.perform()

        lang_button = self.find_element(*self.LANGUAGE_SELECTOR)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_button).perform()
        # sleep(2)
        self.click(*self.RU_LANGUAGE)

    def verify_language_changed(self):
        actual_text = self.find_element(*self.RUSSIAN_HEADER).text
        sleep(2)
        expected_text = 'Главное меню'
        assert expected_text == actual_text, f'Error: expected {expected_text}, is not {actual_text}'

    def click_add_project_option(self):
        self.wait_and_click(*self.ADD_PROJECT_BTN)

    def verify_add_project_page_opens(self):
        self.verify_partial_url('add-a-project')

    def click_community_btn(self):
        self.wait_and_click(*self.COMMUNITY_BTN)

    def click_contact_us_option(self):
        self.wait_and_click(*self.CONTACT_US_BTN)

    def click_user_guide_option(self):
        self.wait_and_click(*self.USER_GUIDE_BTN)

    def click_change_pw_option(self):
        self.wait_and_click(*self.CHANGE_PW_BTN)