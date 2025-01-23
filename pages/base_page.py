from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from support.logger import logger



class Page:
    def __init__(self, driver): # this class will have an access to Selenium driver by and argument, driver. In Pytnon it's done by __init__ you can pass certian functions when this function is created
        self.driver = driver # we're making the Selenium driver visible inside this class, we put it into a variable
        self.wait = WebDriverWait(driver, timeout=15)
        # self is pointing that this driver is now stored inside of this class, inside this page.

    def open_url(self, url):
        # logger.info(f'Opening {url}...') # LINE NEEDED WHEN LOOGING INFO
        self.driver.get(url)

    def find_element(self, *locator):
        # logger.info(f'Searching for element {locator}...') # LINE NEEDED WHEN LOOGING INFO
        return self.driver.find_element(*locator) # besides finding an element we need to return it as well
        # return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator) # besides finding an element we need to return it as well
        # return self.wait.until(EC.presence_of_all_elements_located(locator))


    def click(self, *locator): # in order to click on something we need to know the locator
        # logger.info(f'Clicking element {locator}...') # LINE NEEDED WHEN LOOGING INFO
        self.driver.find_element(*locator).click() # finds the element and clicks

    def input_text(self, text, *locator): # *locator, we need to know the location where to input the text
        # logger.info(f'Inputting text {text} for element {locator}...') # LINE NEEDED WHEN LOOGING INFO
        self.driver.find_element(*locator).send_keys(text) #send_keys to input text

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def get_current_window(self):
        window = self.driver.current_window_handle
        print('Current window:', window)
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        windows = self.driver.window_handles
        print(f'All windows {windows}')
        self.driver.switch_to.window(windows[1])
        print(f'Switched to window => {windows[1]}')

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print(f'Switched to window => {window_id}')

    def close(self):
        self.driver.close()

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        )

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        )

    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        ).click()

    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by locator {locator} did not appear'
        )

    def wait_for_all_visibility_elements_located(self, *locator):
        self.wait.until(
            EC.visibility_of_all_elements_located(locator),
            message=f'Elements by locator {locator} did not appear'
        )

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by locator {locator} shown, but should not appear'
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_partial_text in actual_text, f'Expected {expected_partial_text} not in actual {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f'Expected {expected_partial_url} not in {actual_url}'
