from base_page import BasePage
from locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    # Методы заполнения формы заказа
    def fill_name(self, name):
        name_field = self.find_element(*OrderPageLocators.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)
        return self

    def fill_phone(self, phone):
        phone_field = self.find_element(*OrderPageLocators.PHONE_FIELD)
        phone_field.clear()
        phone_field.send_keys(phone)
        return self

    def submit_order(self):
        submit_button = self.find_element(*OrderPageLocators.SUBMIT_BUTTON)
        submit_button.click()
        return self

    # Методы проверки валидации
    def get_name_error(self):
        return self.find_element(*OrderPageLocators.NAME_ERROR).text

    def get_phone_error(self):
        return self.find_element(*OrderPageLocators.PHONE_ERROR).text

    def is_name_error_present(self):
        return self.is_element_present(*OrderPageLocators.NAME_ERROR)

    def is_phone_error_present(self):
        return self.is_element_present(*OrderPageLocators.PHONE_ERROR)

    # Методы проверки успеха
    def is_success_message_present(self):
        return self.is_element_present(*OrderPageLocators.SUCCESS_MESSAGE)

    def get_success_message(self):
        return self.find_element(*OrderPageLocators.SUCCESS_MESSAGE).text

    # Методы работы с модальным окном
    def close_modal(self):
        close_button = self.find_element(*OrderPageLocators.CLOSE_BUTTON)
        close_button.click()
        return self

    def is_modal_visible(self):
        return self.is_element_visible(*OrderPageLocators.MODAL_WINDOW)

    # Вспомогательные методы
    def wait_for_modal_to_appear(self):
        self.wait_for_element_visibility(*OrderPageLocators.MODAL_WINDOW)
        return self

    def wait_for_modal_to_disappear(self):
        self.wait_for_element_invisibility(*OrderPageLocators.MODAL_WINDOW)
        return self

    def wait_for_success_message(self):
        self.wait_for_element_visibility(*OrderPageLocators.SUCCESS_MESSAGE)
        return self

    # Проверка заполнения полей
    def is_name_field_filled(self):
        return bool(self.find_element(*OrderPageLocators.NAME_FIELD).get_attribute('value'))

    def is_phone_field_filled(self):
        return bool(self.find_element(*OrderPageLocators.PHONE_FIELD).get_attribute('value'))

    # Проверка состояния кнопки отправки
    def is_submit_button_enabled(self):
        return not self.find_element(*OrderPageLocators.SUBMIT_BUTTON).get_attribute('disabled')

    # Проверка состояния формы
    def is_form_valid(self):
        return (
            not self.is_name_error_present() and
            not self.is_phone_error_present() and
            self.is_submit_button_enabled()
        )

    # Метод для полного заполнения формы
    def fill_order_form(self, name, phone):
        self.fill_name(name)
        self.fill_phone(phone)
        return self

    # Метод для отправки заказа с проверкой
    def submit_valid_order(self, name, phone):
        self.fill_order_form(name, phone)
        self.submit_order()
        self.wait_for_success_message()
        return self

    def fill_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)

    def select_metro_station(self, station):
        self.click(OrderPageLocators.STATION_FIELD)
        self.send_keys(OrderPageLocators.STATION_FIELD, station)
        self.find_element(OrderPageLocators.STATION_SUGGESTION).click()

    def select_delivery_date(self, date):
        self.click(OrderPageLocators.DATE_FIELD)
        self.find_element(OrderPageLocators.DATE_OPTION.format(date)).click()

    def select_delivery_time(self, time):
        self.send_keys(OrderPageLocators.TIME_FIELD, time)

    def fill_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)

    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    def click_close_button(self):
        self.click(OrderPageLocators.CLOSE_BUTTON)



