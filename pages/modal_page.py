from locators.modal_locators import ModalPageLocator
from pages.base_page import BasePage


class ModalPage(BasePage):
    def get_modal_title(self):
        title = self.get_element_text(ModalPageLocator.MODAL_TITLE)
        return title

    def get_all_data_from_modal(self):
        data_from_modal = {}
        label = value = ''
        rows = self.find_all_elements(ModalPageLocator.MODAL_TABLE_BODY)
        for i in range(1, len(rows) + 1):
            for j in range(1, 3):
                method, one_cell_locator = ModalPageLocator.CELL
                one_cell_locator = one_cell_locator.format(i, j)
                locator = (method, one_cell_locator)
                cell = self.find_element_with_wait(locator)
                if j == 1:
                    label = cell.text
                else:
                    value = cell.text
                data_from_modal[label] = value
        return data_from_modal

    def check_data_from_modal(self, user):
        result = self.get_all_data_from_modal()
        print(result)
        assert self.get_modal_title() == 'Thanks for submitting the form'
        assert user['first_name'] in result['Student Name'], f'ОР: Имя - {user['first_name']},ФР: {result['Student Name']}'
        assert user['last_name'] in result['Student Name'], f'ОР: Фамилия - {user['last_name']},ФР: {result['Student Name']}'
        assert user['email'] == result['Student Email'], f'ОР: {user['email']},ФР: {result['Student Email']}'
        assert user['gender'] == result['Gender'], f'ОР: {user['gender']},ФР: {result['Gender']}'
        assert str(user['mobile']) == result['Mobile'], f'ОР: {user['mobile']},ФР: {result['Mobile']}'
        assert user['subjects'] == result['Subjects'], f'ОР: {user['subject']},ФР: {result['Subject']}'
        assert result['Picture'] == 'test_image.png', f'ОР: test_image.png,ФР: {result['Picture']}'
        assert user['address'] == result['Address'], f'ОР: {user['address']},ФР: {result['Address']}'
        assert user['state'] in result['State and City'], f'ОР: State - {user['state']},ФР: {result['State and City']}'
        assert user['city'] in result['State and City'], f'ОР: City - {user['city']},ФР: {result['State and City']}'

