from locators.modal_locators import ModalPageLocator
from pages.base_page import BasePage


class ModalPage(BasePage):
    def get_modal_title(self):
        title = self.get_element_text(ModalPageLocator.MODAL_TITLE)
        return title

    def get_all_data_from_modal(self):
        table = {}
        label = value = ''
        rows = self.find_all_elements(ModalPageLocator.MODAL_TABLE_BODY)
        for i in range(1, len(rows)+1):
            for j in range(1,3):
                method, one_cell_locator = ModalPageLocator.CELL
                one_cell_locator = one_cell_locator.format(i, j)
                locator = (method, one_cell_locator)
                cell = self.find_element_with_wait(locator)
                if j == 1:
                    label = cell.text
                else:
                    value = cell.text
                table[label] = value
        print(type(table))
        print(table)
        return table

    def check_data_from_modal(self, user):
        self.get_all_data_from_modal()
        assert self.get_modal_title() == 'Thanks for submitting the form'



