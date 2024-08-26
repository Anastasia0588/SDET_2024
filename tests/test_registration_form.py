import allure

from pages.registration_page import RegistrationPage
from pages.modal_page import ModalPage


class TestRegistration:
    @allure.title('Заполнение формы регистрации')
    def test_registration_success(self, driver, user):
        registration_page = RegistrationPage(driver)
        modal_page = ModalPage(driver)

        registration_page.wait_for_load_page()
        registration_page.fill_name_field(user['first_name'])
        registration_page.fill_last_field(user['last_name'])
        registration_page.fill_email_field(user['email'])
        registration_page.select_any_gender(user)
        registration_page.fill_mobile_field(user['mobile'])
        registration_page.fill_subject_field(user)
        registration_page.upload_image('testdata\\test_image.png')
        registration_page.fill_current_address_field(user['address'])
        registration_page.select_any_state(user)
        registration_page.select_any_city(user)
        registration_page.press_submit_button()

        modal_page.check_data_from_modal(user)
