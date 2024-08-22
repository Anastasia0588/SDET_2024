from pages.registration_page import RegistrationPage


class TestRegistration:
    def test_registration_success(self, driver, user):
        registration_page = RegistrationPage(driver)

        registration_page.wait_for_load_page()
        registration_page.fill_name_field(user['first_name'])
        registration_page.fill_name_field(user['last_name'])
        registration_page.fill_last_field(user['email'])
        registration_page.select_any_gender()
        registration_page.select_birth_date()
