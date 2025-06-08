import pytest
from page_objects.order_page import OrderPage
from page_objects.main_page import MainPage
from page_objects.locators import OrderPageLocators


@pytest.mark.smoke
class TestOrderFlow:
    @pytest.mark.parametrize("order_data", [
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
    ])
    @pytest.mark.parametrize("order_entry_point", ["top_button", "bottom_button"])
    def test_full_order_flow(self, main_page: MainPage, wait, order_data, order_entry_point):
        # Открытие формы заказа
        if order_entry_point == "top_button":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        # Заполнение формы заказа
        order_page = OrderPage(browser)
        order_page.fill_name(order_data["name"])
        order_page.fill_phone(order_data["phone"])
        order_page.fill_address(order_data["address"])
        order_page.select_metro_station(order_data["metro_station"])
        order_page.select_delivery_date(order_data["delivery_date"])
        order_page.select_delivery_time(order_data["delivery_time"])
        order_page.fill_comment(order_data["comment"])
        order_page.click_order_button()

        # Проверка успешного создания заказа
        wait.until(lambda driver: driver.find_element(*OrderPageLocators.SUCCESS_MESSAGE))
        assert order_page.is_success_message_present(), "Сообщение об успешном заказе не появилось"

    def test_logo_navigation(self, main_page: MainPage):
        # Проверка навигации по логотипу Самоката
        main_page.click_scooter_logo()
        assert main_page.is_on_main_page(), "Не удалось перейти на главную страницу Самоката"

        # Проверка навигации по логотипу Яндекса
        main_page.click_yandex_logo()
        assert main_page.is_yandex_zen_open(), "Не удалось перейти на Дзен через логотип Яндекса"
