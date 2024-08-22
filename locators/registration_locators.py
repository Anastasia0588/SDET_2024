from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    # заголовок страницы
    TITLE = By.XPATH, './/h1[text()="Practice Form"]'
    # поле First Name
    FIRST_NAME = By.ID, 'firstName'
    # поле Last Name
    LAST_NAME = By.ID, 'lastName'
    # поле email
    EMAIL = By.ID, 'userEmail'
    # радиобаттон Gender
    GENDER = By.ID, 'gender-radio-{}'
    # поле Date of Birth
    DATE_FIELD = By.ID, 'dateOfBirthInput'

