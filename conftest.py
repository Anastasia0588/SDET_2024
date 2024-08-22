import allure
import pytest
from selenium import webdriver

import links
from helper import generate_random_string


@pytest.fixture(scope='function')
@allure.title('Запуск драйвера')
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome()
    driver.get(links.MAIN_PAGE)
    yield driver
    driver.quit()


@allure.title('Генерация данных пользователя')
@pytest.fixture(scope='function')
def user():
    user = {'first_name': generate_random_string(10),
            'last_name': generate_random_string(12),
            'email': generate_random_string(10) + '@example.com'}

    return user
