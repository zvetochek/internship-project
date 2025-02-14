from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class ContactUsPage(Page):

    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, "a[href*='reelly'].contact-button")
    CONNECT_COMPANY_BTN = (By.XPATH, '//div[text()="Connect the company"]')


    def verify_contact_us_page_opens(self):
        self.verify_url('https://soft.reelly.io/contact-us')

    social_icons = ['Instagram', 'Telegram', 'Youtube', 'Facebook', 'Twitter', 'TikTok', 'Pinterest', 'Snapchat',
                          'LinkedIn']

    def verify_social_media_icons(self):
        icons = self.find_elements(*self.SOCIAL_MEDIA_ICONS)
        # assert len(icons) >= 4, f'Needed at list 4 but got {len(icons)}'
        if icons.count != 4:
            assert icons.count, f"Needs {icons.count} social icons to be present."
        else:
            for icon in icons:
                if icon.text not in self.social_icons:
                    assert icon.text, f"{icon.text} is not a social icon."

    # def verify_social_media_icons(self):
    #     icons = self.find_elements(*self.SOCIAL_MEDIA_ICONS)
    #     assert len(icons) >= 4, f'Needed at list 4 but got {len(icons)}'
    #     # this solution is shorter and works as well without variable 'social_icons'!!

    def verify_connect_the_company_btn(self):
        self.presence_of_element_located(*self.CONNECT_COMPANY_BTN)
        self.wait_until_clickable(*self.CONNECT_COMPANY_BTN)



