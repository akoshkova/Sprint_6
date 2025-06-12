import pytest
from allure import title
from page_objects.order_page import OrderPage
from data import ValidData, InvalidData

class TestOrder:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.order_page = OrderPage(browser)
        self.order_page.open()

    @title('Оформление заказа с валидными данными')
    def test_order_with_valid_data(self):
        self.order_page.fill_form(
            ValidData.name,
            ValidData.phone,
            ValidData.address
        )
        self.order_page.submit_order()
        assert self.order_page.is_order_success()

    @title('Оформление заказа с некорректным именем')
    def test_order_with_invalid_name(self):
        self.order_page.fill_form(
            InvalidData.name_too_short,
            ValidData.phone,
            ValidData.address
        )
        self.order_page.submit_order()
        assert self.order_page.is_name_error_present()

    @title('Оформление заказа с некорректным номером телефона')
    def test_order_with_invalid_phone(self):
        self.order_page.fill_form(
            ValidData.name,
            InvalidData.phone_invalid,
            ValidData.address
        )
        self.order_page.submit_order()
        assert self.order_page.is_phone_error_present()

    @title('Оформление заказа с пустым полем адреса')
    def test_order_with_empty_address(self):
        self.order_page.fill_form(
            ValidData.name,
            ValidData.phone,
            ''
        )
        self.order_page.submit_order()
        assert self.order_page.is_address_error_present()

    @title('Проверка валидации всех полей при пустом заполнении')
    def test_order_with_empty_fields(self):
        self.order_page.submit_order()
        assert self.order_page.is_name_error_present()
        assert self.order_page.is_phone_error_present()
        assert self.order_page.is_address_error_present()

    @title('Проверка закрытия формы заказа')
    def test_close_order_form(self):
        self.order_page.close_form()
        assert self.order_page.is_form_closed()