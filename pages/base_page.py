import autoit
from selenium.webdriver import ActionChains
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

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def scroll_to_element_and_click(self, locator):
        element = self.driver.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def select_any_element(self, locator, num):
        method, one_element_locator = locator
        one_element_locator = one_element_locator.format(num)
        locator = (method, one_element_locator)
        element = self.find_element_with_wait(locator)
        element.click()

    def choose_file(self, file_path, window_title="Open"):
        autoit.win_wait_active(window_title, 5)
        autoit.control_send(window_title, "Edit1", file_path, 0)
        autoit.control_click(window_title, "Button1", 0)


