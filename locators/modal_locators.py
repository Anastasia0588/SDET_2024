from selenium.webdriver.common.by import By


class ModalPageLocator:
    # локатор модального окна
    MODAL = By.XPATH, './/div[@class="modal-content"]'
    # заголовок модального окна
    MODAL_TITLE = By.ID, 'example-modal-sizes-title-lg'
    # локатор ячейки таблицы
    CELL = By.XPATH, './/div[@class="modal-body"]//tbody/tr[{}]/td[{}]'
    # локатор тела таблицы
    MODAL_TABLE_BODY = By.XPATH, './/div[@class="modal-body"]//tbody/tr'


