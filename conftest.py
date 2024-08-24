import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import links
from helper import generate_random_string, generate_mobile_number


@pytest.fixture(scope='function')
@allure.title('Запуск драйвера')
def driver(request):
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--page_load_timeout=10")
    driver = webdriver.Chrome(options=options)
    try:
        driver.set_page_load_timeout(3)
        driver.get(links.MAIN_PAGE)
    except Exception:
        print('Страница грузится дольше 3 сек')
    yield driver
    driver.quit()


@allure.title('Генерация данных пользователя')
@pytest.fixture(scope='function')
def user():
    user = {'first_name': generate_random_string(10),
            'last_name': generate_random_string(12),
            'email': generate_random_string(10) + '@example.com',
            'mobile': generate_mobile_number()}
    return user
