import os

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(locator))

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def fill_text_field(self, locator, text):
        WebDriverWait(self.driver, 10).until((expected_conditions.element_to_be_clickable(locator)))
        self.driver.find_element(*locator).send_keys(text)

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    @allure.step('Прокручиваем страницу до низа')
    def scroll_to_bottom_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def select_any_element(self, locator, num):
        method, one_element_locator = locator
        one_element_locator = one_element_locator.format(num)
        locator = (method, one_element_locator)
        element = self.find_element_with_wait(locator)
        element.click()

    def upload_file(self, element, file):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = current_dir.replace('pages', file)
        print(file_path)
        element.send_keys(file_path)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return element.text

    def find_all_elements(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements
