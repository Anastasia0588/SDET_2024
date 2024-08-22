import allure

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

    def select_any_gender(self):
        self.select_any_element(RegistrationPageLocators.GENDER)

    def select_birth_date(self):
        self.click_on_element(RegistrationPageLocators.DATE_FIELD)
        self.select_any_data()


