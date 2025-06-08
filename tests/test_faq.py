import pytest
from page_objects.faq_page import FaqPage

@pytest.mark.parametrize("question_index", [0, 1, 2, 3])
def test_faq_question_expand(browser, question_index):
    faq_page = FaqPage(browser, browser.base_url + '/faq')
    faq_page.open()
    question_text = faq_page.get_question_text(question_index)
    faq_page.expand_question(question_index)
    assert faq_page.is_answer_visible(question_index), f"Answer for question '{question_text}' is not visible"

@pytest.mark.parametrize("search_term", ["доставка", "оплата", "возврат"])
def test_faq_search(browser, search_term):
    faq_page = FaqPage(browser, browser.base_url + '/faq')
    faq_page.open()
    faq_page.search_faq(search_term)
    results = faq_page.get_search_results()
    assert all(search_term.lower() in result.lower() for result in results), "Search results do not contain search term"

class TestFaq:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.faq_page = FaqPage(browser, browser.base_url + '/faq')
        self.faq_page.open()

    def test_faq_page_loads(self):
        assert self.faq_page.is_page_loaded(), "FAQ page did not load properly"

    def test_faq_questions_count(self):
        questions_count = self.faq_page.get_questions_count()
        assert questions_count >= 5, "There should be at least 5 FAQ questions"

    @pytest.mark.parametrize("sort_by", ["popularity", "recent"])
    def test_faq_sort(self, sort_by):
        self.faq_page.sort_faq_by(sort_by)
        questions = self.faq_page.get_all_questions()
        if sort_by == "popularity":
            assert questions[0] == "Как оформить заказ?", "Most popular question is not displayed first"
        # Add more assertions for different sort types

    @pytest.mark.parametrize("feedback_text", ["Добавить вопрос про возврат", "Улучшить раздел оплаты"])
    def test_faq_feedback(self, feedback_text):
        self.faq_page.send_feedback(feedback_text)
        assert self.faq_page.is_feedback_sent(), "Feedback was not sent successfully"

    @pytest.mark.parametrize("question_id", [1, 2, 3])
    def test_faq_question_details(self, question_id):
        question_text = self.faq_page.get_question_text(question_id)
        self.faq_page.expand_question(question_id)
        assert self.faq_page.is_answer_visible(question_id), f"Answer for question '{question_text}' is not visible"
        assert self.faq_page.get_question_id(question_id) == question_id, "Question ID does not match"

    def test_faq_pagination(self):
        self.faq_page.go_to_next_page()
        assert self.faq_page.is_current_page(2), "Pagination did not work correctly"
        self.faq_page.go_to_previous_page()
        assert self.faq_page.is_current_page(1), "Pagination did not work correctly"

