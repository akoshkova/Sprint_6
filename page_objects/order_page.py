from allure import step
from page_objects.locators import OrderPageLocators
from page_objects.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = '/order'

    @step("Открытие страницы заказа")
    def open(self):
        super().open(self.base_url)

    @step("Заполнение формы заказа")
    def fill_form(self, name, phone, address):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)

    @step("Отправка формы заказа")
    def submit_order(self):
        self.click(OrderPageLocators.SUBMIT_BUTTON)

    @step("Закрытие формы заказа")
    def close_form(self):
        self.click(OrderPageLocators.CLOSE_BUTTON)

    @step("Проверка успешной отправки заказа")
    def is_order_success(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MESSAGE)

    @step("Проверка наличия ошибки в поле имени")
    def is_name_error_present(self):
        return self.is_visible(OrderPageLocators.NAME_ERROR)

    @step("Проверка наличия ошибки в поле телефона")
    def is_phone_error_present(self):
        return self.is_visible(OrderPageLocators.PHONE_ERROR)

    @step("Проверка наличия ошибки в поле адреса")
    def is_address_error_present(self):
        return self.is_visible(OrderPageLocators.ADDRESS_ERROR)

    @step("Проверка закрытия формы")
    def is_form_closed(self):
        return not self.is_visible(OrderPageLocators.ORDER_FORM)

    @step("Проверка валидности формы")
    def is_form_valid(self):
        return (
            not self.is_name_error_present() and
            not self.is_phone_error_present() and
            not self.is_address_error_present()
        )

    @step("Получение текста ошибки в поле имени")
    def get_name_error_text(self):
        return self.get_element_text(OrderPageLocators.NAME_ERROR)

    @step("Получение текста ошибки в поле телефона")
    def get_phone_error_text(self):
        return self.get_element_text(OrderPageLocators.PHONE_ERROR)

    @step("Получение текста ошибки в поле адреса")
    def get_address_error_text(self):
        return self.get_element_text(OrderPageLocators.ADDRESS_ERROR)

    @step("Проверка наличия всех обязательных элементов")
    def is_page_fully_loaded(self):
        return (
            self.is_visible(OrderPageLocators.ORDER_FORM) and
            self.is_visible(OrderPageLocators.NAME_FIELD) and
            self.is_visible(OrderPageLocators.PHONE_FIELD) and
            self.is_visible(OrderPageLocators.ADDRESS_FIELD) and
            self.is_visible(OrderPageLocators.SUBMIT_BUTTON)
        )

    @step("Проверка корректности отображения формы")
    def is_form_displayed_correctly(self):
        return (
            self.is_visible(OrderPageLocators.NAME_FIELD) and
            self.is_visible(OrderPageLocators.PHONE_FIELD) and
            self.is_visible(OrderPageLocators.ADDRESS_FIELD) and
            self.is_visible(OrderPageLocators.SUBMIT_BUTTON)
        )




