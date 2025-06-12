from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import step
from page_objects.locators import BasePageLocators

class BasePage:
    DEFAULT_TIMEOUT = 15
    POLLING_INTERVAL = 0.5

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            self.DEFAULT_TIMEOUT,
            poll_frequency=self.POLLING_INTERVAL
        )

    @step("Открытие страницы")
    def open(self, url):
        self.driver.get(url)

    @step("Нахождение элемента")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @step("Нахождение списка элементов")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @step("Клик по элементу")
    def click(self, locator):
        self.find_element(locator).click()

    @step("Ввод текста")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @step("Проверка видимости элемента")
    def is_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    @step("Ожидание исчезновения элемента")
    def wait_for_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @step("Проверка наличия элемента")
    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    @step("Получение текста элемента")
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @step("Получение атрибута элемента")
    def get_element_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    @step("Проверка наличия ошибки")
    def is_error_present(self, locator):
        return self.is_visible(locator) and self.get_element_text(locator) != ''

    @step("Ожидание появления элемента")
    def wait_for_element_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @step("Ожидание кликабельности элемента")
    def wait_for_element_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    @step("Проверка URL страницы")
    def is_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    @step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @step("Проверка заголовка страницы")
    def is_page_title(self, expected_title):
        return self.driver.title == expected_title

    @step("Получение заголовка страницы")
    def get_page_title(self):
        return self.driver.title

    @step("Проверка наличия сообщения об успехе")
    def is_success_message_present(self, locator):
        return self.is_visible(locator) and self.get_element_text(locator).lower().find('успешно') != -1

    @step("Проверка загрузки страницы")
    def is_page_loaded(self):
        return self.is_visible(BasePageLocators.PAGE_LOAD_INDICATOR)

    @step("Проверка наличия заголовка страницы")
    def has_page_header(self):
        return self.is_visible(BasePageLocators.PAGE_HEADER)

    @step("Проверка наличия футера страницы")
    def has_page_footer(self):
        return self.is_visible