import random

import allure

from helper import random_year_of_birth, locator_with_param
from locators.registration_locators import RegistrationPageLocators
from pages.base_page import BasePage
from testdata.testdata import subject_list


class RegistrationPage(BasePage):
    def wait_for_load_page(self):
        self.wait_element(RegistrationPageLocators.TITLE)

    @allure.step('Заполняем поле First name')
    def fill_name_field(self, first_name):
        self.fill_text_field(RegistrationPageLocators.FIRST_NAME, first_name)

    @allure.step('Заполняем поле Last name')
    def fill_last_field(self, last_name):
        self.fill_text_field(RegistrationPageLocators.LAST_NAME, last_name)

    @allure.step('Заполняем поле Email')
    def fill_email_field(self, email):
        self.fill_text_field(RegistrationPageLocators.EMAIL, email)

    @allure.step('Заполняем поле Mobile number')
    def fill_mobile_field(self, mobile):
        self.fill_text_field(RegistrationPageLocators.MOBILE, mobile)

    @allure.step('Выбираем любой Gender')
    def select_any_gender(self, user):
        selected_gender = self.select_any_element(RegistrationPageLocators.GENDERS, random.randint(1, 3))
        user['gender'] = selected_gender.text

    @allure.step('Выбираем дату из календаря')
    def select_birth_date(self):
        self.click_on_element(RegistrationPageLocators.DATE_FIELD)
        self.click_on_element(RegistrationPageLocators.YEAR_DROPDOWN)
        self.select_year(RegistrationPageLocators.YEAR)

    def select_year(self, locator):
        year_locator = locator_with_param(locator, random_year_of_birth())
        self.scroll_to_element(year_locator)

    @allure.step('Заполняем поле Subject')
    def fill_subject_field(self, user):
        subject = random.choice(subject_list)
        self.fill_text_field(RegistrationPageLocators.SUBJECTS, subject)
        subject_locator = locator_with_param(RegistrationPageLocators.SUBJECT_FROM_LIST, subject)
        self.click_on_element(subject_locator)
        user['subjects'] = subject

    @allure.step('Заполняем поле Current Address')
    def fill_current_address_field(self, address):
        self.fill_text_field(RegistrationPageLocators.CURRENT_ADDRESS, address)

    @allure.step('Загружаем картинку')
    def upload_image(self, file):
        input_file = self.find_element_with_wait(RegistrationPageLocators.INPUT_FILE)
        self.upload_file(input_file, file)

    @allure.step('Нажимаем кнопку Submit')
    def press_submit_button(self):
        self.scroll_to_bottom_page()
        self.click_on_element(RegistrationPageLocators.SUBMIT_BTN)

    @allure.step('Выбираем любой штат из выпадающего списка Select State')
    def select_any_state(self, user):
        self.click_on_element(RegistrationPageLocators.SELECT_STATE)
        self.select_any_element(RegistrationPageLocators.STATE, random.randint(0, 3))
        user["state"] = self.get_element_text(RegistrationPageLocators.SELECTED_STATE)

    @allure.step('Выбираем любой город из выпадающего списка Select City')
    def select_any_city(self, user):
        self.click_on_element(RegistrationPageLocators.SELECT_CITY)
        cities_list = self.find_all_elements(RegistrationPageLocators.CITIES)
        self.select_any_element(RegistrationPageLocators.CITY, random.randint(0, len(cities_list)))
        user["city"] = self.get_element_text(RegistrationPageLocators.SELECTED_CITY)

