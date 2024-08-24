import random

import allure

from helper import random_year_of_birth, generate_random_string, generate_address
from locators.registration_locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def wait_for_load_page(self):
        self.wait_element(RegistrationPageLocators.TITLE)

    @allure.step('Заполняем поле First name')
    def fill_name_field(self, first_name):
        self.fill_text_field(RegistrationPageLocators.FIRST_NAME, first_name)

    def fill_last_field(self, last_name):
        self.fill_text_field(RegistrationPageLocators.LAST_NAME, last_name)

    def fill_email_field(self, email):
        self.fill_text_field(RegistrationPageLocators.EMAIL, email)

    def fill_mobile_field(self, mobile):
        self.fill_text_field(RegistrationPageLocators.MOBILE, mobile)

    def select_any_gender(self):
        self.select_any_element(RegistrationPageLocators.GENDERS, random.randint(1, 3))

    def select_birth_date(self):
        self.click_on_element(RegistrationPageLocators.DATE_FIELD)
        self.click_on_element(RegistrationPageLocators.YEAR_DROPDOWN)
        self.select_year(RegistrationPageLocators.YEAR)

    def select_year(self, locator):
        method, year_locator = locator
        year_locator = year_locator.format(random_year_of_birth())
        locator = (method, year_locator)
        self.scroll_to_element_and_click(locator)

    def fill_subject_field(self):
        self.fill_text_field(RegistrationPageLocators.SUBJECTS, generate_random_string(50))

    def fill_current_address_field(self):
        address = generate_address()
        self.fill_text_field(RegistrationPageLocators.CURRENT_ADDRESS, address)

    def upload_image(self, file):
        input_file = self.find_element_with_wait(RegistrationPageLocators.INPUT_FILE)
        self.upload_file(input_file, file)

    def press_submit_button(self):
        self.scroll_to_bottom_page()
        self.click_on_element(RegistrationPageLocators.SUBMIT_BTN)






