from pages.base_page import Page
# from pages.header import Header
from pages.main_page import MainPage
# from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.settings_page import SettingsPage
from pages.subscrip_paym_page import SubscrPaymentPage

class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.sign_in_page = SignInPage(driver)
        # self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.subscrip_paym_page = SubscrPaymentPage(driver)
        # self.search_results_page = SearchResultsPage(driver)
