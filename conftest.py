import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.base_page import BasePage

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser", default="chrome")
    driver = None

    try:
        if browser_name == "chrome":
            options = Options()
            options.add_argument("--start-maximized")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Браузер {browser_name} не поддерживается")

        yield driver

    finally:
        if driver:
            driver.quit()

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)


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

