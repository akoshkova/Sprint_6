import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.base_page import BasePage

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    yield driver
    driver.quit()

@pytest.fixture
def base_page(driver):
    return BasePage(driver)


# Фикстура для тестовых данных заказа
@pytest.fixture
def order_data():
    return [
        {
            "name": "Иван Петров",
            "phone": "+79991234567",
            "address": "г. Москва, ул. Ленина, д. 1",
            "metro_station": "ВДНХ",
            "delivery_date": "завтра",
            "delivery_time": "12:00",
            "comment": "Доставить до двери"
        },
        {
            "name": "Анна Смирнова",
            "phone": "+79997654321",
            "address": "г. Санкт-Петербург, пр. Ленина, д. 2",
            "metro_station": "Технологический институт",
            "delivery_date": "послезавтра",
            "delivery_time": "14:00",
            "comment": "Оставить у двери"
        }
    ]

