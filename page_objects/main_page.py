from page_objects.base_page import BasePage
from page_objects.locators import MainPageLocators, BasePageLocators
from allure import step

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @step("Открытие ответа FAQ")
    def open_faq_answer(self, question_index):
        question = self.find_elements(MainPageLocators.FAQ_QUESTIONS)[question_index]
        question.click()
        return self.find_element(MainPageLocators.FAQ_ANSWERS)

    @step("Клик по логотипу")
    def click_self_logo(self):
        self.click(MainPageLocators.SELF_LOGO)

    @step("Открытие формы заказа")
    def open_order_form(self, top=True):
        if top:
            self.click(MainPageLocators.ORDER_BUTTON_TOP)
        else:
            self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @step("Проверка видимости шапки")
    def is_header_visible(self):
        return self.is_element_present(MainPageLocators.MAIN_HEADER)

    @step("Проверка видимости футера")
    def is_footer_visible(self):
        return self.is_element_present(MainPageLocators.FOOTER)

    @step("Проверка видимости спиннера загрузки")
    def is_loading_spinner_visible(self):
        return self.is_element_present(BasePageLocators.LOADING_SPINNER)

    @step("Ожидание появления уведомления")
    def wait_for_notification(self):
        self.wait_for_element_visibility(BasePageLocators.NOTIFICATION_BAR)

    @step("Клик по верхней кнопке заказа")
    def click_top_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @step("Клик по нижней кнопке заказа")
    def click_bottom_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @step("Клик по логотипу Яндекс")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)


    @step("Проверка видимости формы заказа")
    def is_order_form_visible(self):
        return self.is_element_present(MainPageLocators.ORDER_FORM)

    @step("Проверка наличия верхней кнопки заказа")
    def is_top_order_button_present(self):
        return self.is_element_present(MainPageLocators.ORDER_BUTTON_TOP)

    @step("Проверка наличия нижней кнопки заказа")
    def is_bottom_order_button_present(self):
        return self.is_element_present(MainPageLocators.ORDER_BUTTON_BOTTOM)

    # Вспомогательные методы для работы с FAQ
    @step("Получение всех вопросов FAQ")
    def get_all_faq_questions(self):
        return [question.text for question in self.find_elements(MainPageLocators.FAQ_QUESTIONS)]

    @step("Получение текста конкретного вопроса FAQ")
    def get_faq_question_text(self, index):
        return self.find_elements(MainPageLocators.FAQ_QUESTIONS)[index].text

    @step("Проверка загрузки страницы")
    def is_page_loaded(self):
        return self.is_visible(MainPageLocators.PAGE_LOAD_INDICATOR)

    @step("Проверка наличия заголовка страницы")
    def has_page_header(self):
        return self.is_visible(MainPageLocators.PAGE_HEADER)


