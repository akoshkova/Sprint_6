from base_page import BasePage
from locators import FaqPageLocators as loc


class FaqPage(BasePage):
    def open(self):
        self.browser.get(self.url)

    def is_page_loaded(self):
        return self.is_element_present(*loc.FAQ_HEADER)

    def get_questions_count(self):
        return len(self.browser.find_elements(*loc.FAQ_QUESTIONS))

    def get_question_text(self, index):
        return self.browser.find_elements(*loc.FAQ_QUESTIONS)[index].text

    def expand_question(self, index):
        question = self.browser.find_elements(*loc.FAQ_QUESTIONS)[index]
        question.click()

    def is_answer_visible(self, index):
        answer = self.browser.find_elements(*loc.FAQ_ANSWERS)[index]
        return answer.is_displayed()

    def search_faq(self, search_term):
        self.browser.find_element(*loc.SEARCH_INPUT).send_keys(search_term)
        self.browser.find_element(*loc.SEARCH_BUTTON).click()

    def get_search_results(self):
        return [result.text for result in self.browser.find_elements(*loc.SEARCH_RESULTS)]

    def sort_faq_by(self, sort_type):
        if sort_type == "popularity":
            self.browser.find_element(*loc.SORT_POPULARITY).click()
        elif sort_type == "recent":
            self.browser.find_element(*loc.SORT_RECENT).click()

    def send_feedback(self, feedback_text):
        self.browser.find_element(*loc.FEEDBACK_INPUT).send_keys(feedback_text)
        self.browser.find_element(*loc.FEEDBACK_BUTTON).click()

    def is_feedback_sent(self):
        return self.is_element_present(*loc.FEEDBACK_SUCCESS)

    def go_to_next_page(self):
        self.browser.find_element(*loc.NEXT_PAGE).click()

    def go_to_previous_page(self):
        self.browser.find_element(*loc.PREVIOUS_PAGE).click()

    def is_current_page(self, page_number):
        current_page = self.browser.find_element(*loc.CURRENT_PAGE).text
        return int(current_page) == page_number

    def get_question_id(self, index):
        return self.browser.find_elements(*loc.FAQ_QUESTIONS)[index].get_attribute('data-id')
