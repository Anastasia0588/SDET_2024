from locators.submit_page_locators import SubmitPageLocator
from pages.base_page import BasePage


class SubmitWindow(BasePage):
    def get_popup_title(self):
        title = self.get_element_text(SubmitPageLocator.SUBMIT_POPUP_WINDOW)
        return title
