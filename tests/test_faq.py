import pytest
from helpers import verify_search_results
from page_objects.faq_page import FaqPage
from allure import title

class TestFaq:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.faq_page = FaqPage(driver)
        self.faq_page.open()

    @title("Проверка загрузки страницы FAQ")
    def test_faq_page_loads(self):
        assert self.faq_page.is_page_loaded(), "FAQ page did not load properly"

    @title("Проверка количества вопросов FAQ")
    def test_faq_questions_count(self):
        questions_count = self.faq_page.get_questions_count()
        assert questions_count >= 5, "There should be at least 5 FAQ questions"

    @title("Проверка сортировки FAQ по популярности")
    def test_faq_sort_by_popularity(self):
        self.faq_page.sort_faq_by("popularity")
        questions = self.faq_page.get_all_questions()
        assert len(questions) > 0, "No questions displayed after sorting"

    @title("Проверка сортировки FAQ по новизне")
    def test_faq_sort_by_recent(self):
        self.faq_page.sort_faq_by("recent")
        questions = self.faq_page.get_all_questions()
        assert len(questions) > 0, "No questions displayed after sorting"



    @pytest.mark.parametrize("feedback_text", ["Добавить вопрос про возврат", "Улучшить раздел оплаты"])
    @title("Проверка отправки обратной связи")
    def test_faq_feedback(self, feedback_text):
        self.faq_page.send_feedback(feedback_text)
        assert self.faq_page.is_feedback_sent(), "Feedback was not sent successfully"

    @pytest.mark.parametrize("question_id", [1, 2, 3])
    @title("Проверка деталей вопроса FAQ")
    def test_faq_question_details(self, question_id):
        question_text = self.faq_page.get_question_text(question_id)
        self.faq_page.expand_question(question_id)
        assert self.faq_page.is_answer_visible(question_id), f"Answer for question '{question_text}' is not visible"
        assert self.faq_page.get_question_id(question_id) == question_id, "Question ID does not match"

    @title("Проверка пагинации FAQ")
    def test_faq_pagination(self):
        self.faq_page.go_to_next_page()
        assert self.faq_page.is_current_page(2), "Pagination did not work correctly"
        self.faq_page.go_to_previous_page()
        assert self.faq_page.is_current_page(1), "Pagination did not work correctly"

    @pytest.mark.parametrize("question_index", [0, 1, 2, 3])
    @title("Проверка раскрытия вопроса FAQ")
    def test_faq_question_expand(self, question_index):
        question_text = self.faq_page.get_question_text(question_index)
        self.faq_page.expand_question(question_index)
        assert self.faq_page.is_answer_visible(question_index), f"Answer for question '{question_text}' is not visible"

    @pytest.mark.parametrize("search_term", ["доставка", "оплата", "возврат"])
    @title("Проверка поиска в FAQ")
    def test_faq_search(self, search_term):
        self.faq_page.search_faq(search_term)
        results = self.faq_page.get_search_results()
        verify_search_results(search_term, results)
