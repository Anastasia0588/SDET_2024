from pages.registration_page import RegistrationPage
from pages.submit_page import SubmitWindow


class TestRegistration:
    def test_registration_success(self, driver, user):
        registration_page = RegistrationPage(driver)
        submit_window = SubmitWindow(driver)

        registration_page.wait_for_load_page()
        registration_page.fill_name_field(user['first_name'])
        registration_page.fill_last_field(user['last_name'])
        registration_page.fill_email_field(user['email'])
        registration_page.select_any_gender()
        registration_page.fill_mobile_field(user['mobile'])
        registration_page.fill_subject_field()
        registration_page.upload_image('testdata\\test_image.png')
        registration_page.fill_current_address_field()
        registration_page.press_submit_button()

        popup_title = submit_window.get_popup_title()
        assert popup_title == 'Thanks for submitting the form'

        #        registration_page.select_birth_date()
