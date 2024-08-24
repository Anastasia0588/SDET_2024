from selenium.webdriver.common.by import By


class SubmitPageLocator:
    # локатор popup окна
    POPUP_WINDOW = By.XPATH, './/div[@class="modal-content"]'
    #
    SUBMIT_POPUP_WINDOW = By.ID, 'example-modal-sizes-title-lg'

