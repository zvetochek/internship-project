from pages.base_page import Page
# from pages.header import Header
from pages.add_project_page import AddProjectPage
from pages.change_pw_page import ChangePwPage
from pages.community_page import CommunityPage
from pages.contact_us_page import ContactUsPage
from pages.edit_profile_page import EditProfilePage
from pages.main_page import MainPage
from pages.market_page import MarketPage
# from pages.search_results_page import SearchResultsPage
from pages.off_plan_page import OffPlanPage
from pages.registr_page import RegistrPage
from pages.secondary_page import SecondaryPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import SignInPage
from pages.subscrip_paym_page import SubscrPaymentPage
from pages.support_page import SupportPage
from pages.user_guide_page import UserGuidePage
from pages.verification_page import VerificationPage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.add_project_page = AddProjectPage(driver)
        self.change_pw_page = ChangePwPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.community_page = CommunityPage(driver)
        self.edit_profile_page = EditProfilePage(driver)
        self.main_page = MainPage(driver)
        self.market_page = MarketPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.registr_page = RegistrPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SignInPage(driver)
        # self.header = Header(driver)
        self.subscrip_paym_page = SubscrPaymentPage(driver)
        self.support_page = SupportPage(driver)
        self.user_guide_page = UserGuidePage(driver)
        self.verification_page = VerificationPage(driver)
        # self.search_results_page = SearchResultsPage(driver)

        ## Lana's video how to activate the New License for PyCharm:
        ## https://www.youtube.com/embed/iINprFKknQA