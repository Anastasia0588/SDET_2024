import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(locator))

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def fill_text_field(self, locator, text):
        WebDriverWait(self.driver, 5).until((expected_conditions.element_to_be_clickable(locator)))
        self.driver.find_element(*locator).send_keys(text)

    def select_any_element(self, locator):
        method, locator = locator
        selected_element_locator = locator.format(random.randint(0, 2))
        self.find_element_with_wait((method, selected_element_locator)).click()

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

