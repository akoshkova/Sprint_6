from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from base_page import BasePage
from locators import MainPageLocators, BasePageLocators


class MainPage(BasePage):
    def __init__(self, browser, url):
       super().__init__(browser, url)

    # Методы для работы с FAQ
    def get_faq_questions(self):
       return self.find_elements(*MainPageLocators.FAQ_QUESTIONS)

    def open_faq_answer(self, question_index):
        questions = self.get_faq_questions()
        questions[question_index].click()
        return self.find_element(*MainPageLocators.FAQ_ANSWERS)

    # Методы для навигации
    def click_self_logo(self):
        self.find_element(*MainPageLocators.SELF_LOGO).click()


    # Методы для заказа
    def open_order_form(self, top=True):
        if top:
            self.find_element(*MainPageLocators.ORDER_BUTTON_TOP).click()
        else:
            self.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM).click()

    # Методы проверки элементов
    def is_header_visible(self):
        return self.find_element(*MainPageLocators.MAIN_HEADER).is_displayed()

    def is_footer_visible(self):
        return self.find_element(*MainPageLocators.FOOTER).is_displayed()

    def is_loading_spinner_visible(self):
        return self.find_element(*BasePageLocators.LOADING_SPINNER).is_displayed()

    # Методы ожидания
    def wait_for_loading_to_finish(self):
        self.wait_until_not_visible(*BasePageLocators.LOADING_SPINNER)

    def wait_for_notification(self):
        self.wait_until_visible(*BasePageLocators.NOTIFICATION_BAR)

    # Вспомогательные методы
    def wait_until_visible(self, by, value):
        WebDriverWait(self.browser, 10).until(
        EC.visibility_of_element_located((by, value))
        )

    def wait_until_not_visible(self, by, value):
        WebDriverWait(self.browser, 10).until_not(
        EC.visibility_of_element_located((by, value))
        )

    def get_current_url(self):
        return self.browser.current_url

    def refresh_page(self):
        self.browser.refresh()

    def get_page_title(self):
        return self.browser.title

    def is_element_present(self, by):
        try:
            self.find_element(by)
            return True
        except NoSuchElementException:
            return False

    def scroll_to_element(self, by):
        element = self.find_element(by)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def get_element_text(self, by, value):
        return self.find_element(by).text

    def get_element_attribute(self, by, value, attribute):
        return self.find_element(by).get_attribute(attribute)

    def click_top_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_bottom_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SELF_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def is_on_main_page(self):
        return self.browser.current_url.endswith("/")

    def is_yandex_zen_open(self):
        return "zen.yandex.ru" in self.browser.current_url

    def is_order_form_visible(self):
        return self.is_element_present(MainPageLocators.ORDER_FORM)

    def is_top_order_button_present(self):
        return self.is_element_present(MainPageLocators.ORDER_BUTTON_TOP)

    def is_bottom_order_button_present(self):
        return self.is_element_present(MainPageLocators.ORDER_BUTTON_BOTTOM)