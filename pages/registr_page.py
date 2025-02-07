from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep


class RegistrPage(Page):

    FULL_NAME = (By.ID, "Full-Name")
    PHONE = (By.ID, "phone2")
    EMAIL = (By.ID, "Email-3")
    PASSWORD = (By.ID, "field")
    COMPANY_NAME = (By.ID, "Company-website")
    ROLE = (By.ID, "Role")
    POSITION = (By.ID, "Position")
    COUNTRY = (By.ID, "country-select")
    COMPANY_SIZE = (By.ID, "Agents-amount-2")
    PP_CHECKBOX = (By.ID, "checkbox")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".login-button")


    def open_registr_page(self):
        self.open_url('https://soft.reelly.io/sign-up')

    def enter_registr_info(self):
        self.input_text("Monika", *self.FULL_NAME)
        self.input_text("0001112223", *self.PHONE)
        self.clear_text(*self.EMAIL)
        self.input_text("data@info.com", *self.EMAIL)
        self.clear_text(*self.PASSWORD)
        self.input_text("test123", *self.PASSWORD)
        self.input_text("test", *self.COMPANY_NAME)
        self.select_dropdown_value('Broker', *self.ROLE)
        self.select_dropdown_value('Seller / Manager', *self.POSITION )
        self.select_dropdown_value('United States of America', *self.COUNTRY)
        self.select_dropdown_value('50-100', *self.COMPANY_SIZE)
        self.checkbox_click(*self.PP_CHECKBOX)

    def verify_registr_info(self):
        self.verify_attribute_value("Monika", *self.FULL_NAME)
        self.verify_attribute_value("0001112223", *self.PHONE)
        self.verify_attribute_value("data@info.com", *self.EMAIL)
        self.verify_attribute_value("test123", *self.PASSWORD)
        self.verify_attribute_value("test", *self.COMPANY_NAME)
        self.get_dropdown_value('Broker', *self.ROLE)
        self.get_dropdown_value('Seller / Manager', *self.POSITION)
        self.get_dropdown_value('United States of America', *self.COUNTRY)
        self.get_dropdown_value('50-100', *self.COMPANY_SIZE)
        self.is_checkbox_selected(*self.PP_CHECKBOX)
