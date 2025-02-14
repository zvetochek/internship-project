from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep


class AddProjectPage(Page):


    ADD_NAME = (By.ID, "Your-name")
    ADD_COMPANY_NAME = (By.ID, "Your-company-name")
    ADD_ROLE =(By.ID, "Role")
    ADD_COMPANY_AGE=(By.ID, "Age-of-the-company")
    ADD_LOCATION = (By.ID, "Country")
    ADD_PROJECT_NAME = (By.ID, "Name-project")
    ADD_PHONE =(By.ID, "Phone")
    ADD_EMAIL=(By.ID, "Email-add-project")
    SEND_AN_APPLICATION_BTN = (By.CSS_SELECTOR, "input[value='Send an application']")

    def add_test_information(self):
        self.input_text("Lisa", *self.ADD_NAME)
        self.input_text("TestDevelopers", *self.ADD_COMPANY_NAME)
        self.input_text("AQA", *self.ADD_ROLE)
        self.input_text("15", *self.ADD_COMPANY_AGE)
        self.input_text("USA", *self.ADD_LOCATION)
        self.input_text("Internship", *self.ADD_PROJECT_NAME)
        self.input_text("111-111-1111", *self.ADD_PHONE)
        self.input_text("adding@test.com", *self.ADD_EMAIL)

    def verify_right_information_present(self):
        self.verify_attribute_value("Lisa", *self.ADD_NAME)
        self.verify_attribute_value("TestDevelopers", *self.ADD_COMPANY_NAME)
        self.verify_attribute_value("AQA", *self.ADD_ROLE)
        self.verify_attribute_value("15", *self.ADD_COMPANY_AGE)
        self.verify_attribute_value("USA", *self.ADD_LOCATION)
        self.verify_attribute_value("Internship", *self.ADD_PROJECT_NAME)
        self.verify_attribute_value("111-111-1111", *self.ADD_PHONE)
        self.verify_attribute_value("adding@test.com", *self.ADD_EMAIL)

    def verify_send_application_btn(self):
        self.presence_of_element_located(*self.SEND_AN_APPLICATION_BTN)
        self.wait_until_clickable(*self.SEND_AN_APPLICATION_BTN)
