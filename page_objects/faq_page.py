from allure import step
from page_objects.locators import FaqPageLocators
from page_objects.base_page import BasePage

class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FaqPageLocators

    @step("Открытие страницы FAQ")
    def open(self):
        super().open(self.base_url)

    @step("Получение текста вопроса")
    def get_question_text(self, index):
        return self.get_element_text(FaqPageLocators.QUESTION_TEXT.format(index=index))

    @step("Раскрытие вопроса")
    def expand_question(self, index):
        self.click(FaqPageLocators.QUESTION_EXPAND_BUTTON.format(index=index))

    @step("Проверка видимости ответа")
    def is_answer_visible(self, index):
        return self.is_visible(FaqPageLocators.ANSWER_TEXT.format(index=index))

    @step("Получение количества вопросов")
    def get_questions_count(self):
        return len(self.find_elements(FaqPageLocators.QUESTION_ITEMS))

    @step("Сортировка FAQ")
    def sort_faq_by(self, sort_by):
        self.click(FaqPageLocators.SORT_BY.format(sort_by=sort_by))

    @step("Отправка обратной связи")
    def send_feedback(self, text):
        self.send_keys(FaqPageLocators.FEEDBACK_INPUT, text)
        self.click(FaqPageLocators.FEEDBACK_SUBMIT)

    @step("Проверка отправки обратной связи")
    def is_feedback_sent(self):
        return self.is_visible(FaqPageLocators.FEEDBACK_SUCCESS)

    @step("Поиск по FAQ")
    def search_faq(self, term):
        self.send_keys(FaqPageLocators.SEARCH_INPUT, term)
        self.click(FaqPageLocators.SEARCH_BUTTON)

    @step("Получение результатов поиска")
    def get_search_results(self):
        return [elem.text for elem in self.find_elements(FaqPageLocators.SEARCH_RESULTS)]

    @step("Переход на следующую страницу")
    def go_to_next_page(self):
        self.click(FaqPageLocators.NEXT_PAGE)

    @step("Переход на предыдущую страницу")
    def go_to_previous_page(self):
        self.click(FaqPageLocators.PREV_PAGE)

    @step("Проверка текущей страницы")
    def is_current_page(self, page_number):
        return self.get_element_text(FaqPageLocators.CURRENT_PAGE) == str(page_number)

    @step("Проверка наличия всех обязательных элементов")
    def is_page_loaded(self):
        return (
            self.is_visible(FaqPageLocators.FAQ_HEADER) and
            self.is_visible(FaqPageLocators.SEARCH_FORM) and
            self.is_visible(FaqPageLocators.SORT_OPTIONS) and
            self.is_visible(FaqPageLocators.QUESTION_LIST)
        )

    @step("Проверка наличия всех вопросов")
    def are_all_questions_present(self):
        return self.get_questions_count() > 0

    @step("Проверка корректности отображения FAQ")
    def is_faq_displayed_correctly(self):
        for i in range(1, self.get_questions_count()+1):
            if not self.is_visible(FaqPageLocators.QUESTION_TEXT.format(index=i)):
                return False
        return True

    @step("Получение ID вопроса по индексу")
    def get_question_id(self, index):
        return self.get_element_attribute(FaqPageLocators.QUESTION_ITEMS.format(index=index), 'id')