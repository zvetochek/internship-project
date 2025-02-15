from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class UserGuidePage(Page):

    # VIDEO_TITLES = (By.CSS_SELECTOR, "a[data-sessionlink='feature=player-title']")
    LESSON_TITLES = (By.CSS_SELECTOR, "a.ytp-title-link.yt-uix-sessionlink")
    # IFRAME1 = (By.CSS_SELECTOR, "div.video-2.w-video.w-embed iframe.embedly-embed")
    # IFRAME2 = (By.CSS_SELECTOR, "#player")


    def verify_user_guide_page_opens(self):
        self.verify_url('https://soft.reelly.io/user-guide')

    def verify_videos_have_titles(self):
        lesson_titles = self.find_elements(*self.LESSON_TITLES)
        for title in lesson_titles:
            assert title.text, f'Video lesson does not have a title for {title.text}'

        # WORKING WITH iFrames!!
        #  switch the frames
        # self.switch_frames(*self.IFRAME1)
        #
        # self.switch_frames(*self.IFRAME2)
        #
        # # get all titles
        # video_titles = self.driver.find_elements(*self.VIDEO_TITLES)
        # print(len(video_titles))
        # for title in video_titles:
        #     print(title.text)
        #     self.presence_of_element_located(*self.VIDEO_TITLES)
        #
        # # switch back to default.
        # self.reset_frame()
