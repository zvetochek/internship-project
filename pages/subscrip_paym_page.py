from pages.base_page import Page
from selenium.webdriver.common.by import By


class SubscrPaymentPage(Page):

    SUBSCR_PAYM_TEXT = (By.CSS_SELECTOR, ".lotion-your-h3--price.size")
    # BACK_BTN = (By.CSS_SELECTOR, "a[href='/settings'].button-verify")
    BACK_BTN = (By.CSS_SELECTOR,"a[href='/settings']")
    UPGRADE_PLAN_BTN = (By.CSS_SELECTOR, "a[wized='upgradePlanButton']")

    def verify_subs_paym_url(self):
        self.verify_url('https://soft.reelly.io/subscription')

    def verify_sp_title_visible(self):
        self.verify_text('Subscription & payments', *self.SUBSCR_PAYM_TEXT)

    def verify_buttons_displayed(self):
        self.verify_text('Back', *self.BACK_BTN)
        self.verify_text('Upgrade plan', *self.UPGRADE_PLAN_BTN)