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
    # поле Mobile
    MOBILE = By.ID, 'userNumber'
    # радиобаттон Gender
    GENDERS = By.XPATH, './/input[@id="gender-radio-{}"]/following-sibling::label' # gender-radio-{}
    # поле Date of Birth
    DATE_FIELD = By.ID, 'dateOfBirthInput'
    # календарь
    YEAR_DROPDOWN = By.XPATH, '//div[@id="dateOfBirth"]//select[contains(@class, "react-datepicker__year-select")]'
    YEAR = By.XPATH, '//div[@id="dateOfBirth"]//options[@value="{}"]'
    # поле Subjects
    SUBJECTS = By.ID, 'subjectsInput'
    # поле Current Address
    CURRENT_ADDRESS = By.ID, 'currentAddress'
    # поле загрузки файла
    INPUT_FILE = By.ID, 'uploadPicture'
    # кнопка Submit
    SUBMIT_BTN = By.ID, 'submit'



