from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".order-button.top")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".order-button.bottom")
    ORDER_FORM = (By.CSS_SELECTOR, ".order-form")

    # FAQ
    FAQ_QUESTIONS = (By.CSS_SELECTOR, ".faq-question")
    FAQ_ANSWERS = (By.CSS_SELECTOR, ".faq-answer")

    # Логотипы
    SELF_LOGO = (By.CSS_SELECTOR, ".logo.self")
    YANDEX_LOGO = (By.CSS_SELECTOR, ".logo.yandex")

    # Базовые элементы
    MAIN_HEADER = (By.CSS_SELECTOR, ".main-header")
    MAIN_CONTENT = (By.CSS_SELECTOR, ".main-content")
    FOOTER = (By.CSS_SELECTOR, ".footer")


class OrderPageLocators:
    # Поля ввода
    NAME_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name='phone']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "input[name='address']")
    STATION_FIELD = (By.CSS_SELECTOR, "input[name='station']")
    DATE_FIELD = (By.CSS_SELECTOR, "input[name='date']")
    TIME_FIELD = (By.CSS_SELECTOR, "input[name='time']")
    COMMENT_FIELD = (By.CSS_SELECTOR, "textarea[name='comment']")

    # Кнопки
    ORDER_BUTTON = (By.CSS_SELECTOR, ".order-button")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".close-button")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".submit-button")

    # Модальное окно
    MODAL_WINDOW = (By.CSS_SELECTOR, ".modal-window")

    # Сообщение об успехе
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message")

    # Подсказки и ошибки
    STATION_SUGGESTION = (By.CSS_SELECTOR, ".station-suggestion")
    DATE_OPTION = (By.CSS_SELECTOR, ".date-option[data-date='{}']")

    # Ошибки валидации
    NAME_ERROR = (By.CSS_SELECTOR, ".name-error")
    PHONE_ERROR = (By.CSS_SELECTOR, ".phone-error")
    ADDRESS_ERROR = (By.CSS_SELECTOR, ".address-error")
    STATION_ERROR = (By.CSS_SELECTOR, ".station-error")
    DATE_ERROR = (By.CSS_SELECTOR, ".date-error")
    TIME_ERROR = (By.CSS_SELECTOR, ".time-error")
    COMMENT_ERROR = (By.CSS_SELECTOR, ".comment-error")

    # Дополнительные элементы
    TRACKING_NUMBER = (By.CSS_SELECTOR, ".tracking-number")
    DELIVERY_STATUS = (By.CSS_SELECTOR, ".delivery-status")
    ESTIMATED_DELIVERY = (By.CSS_SELECTOR, ".estimated-delivery")
    CARRIER_INFO = (By.CSS_SELECTOR, ".carrier-info")
    ORDER_ID = (By.CSS_SELECTOR, ".order-id")

    # Элементы для отслеживания статуса
    TRACKING_PAGE = (By.CSS_SELECTOR, ".tracking-page")
    TRACKING_FORM = (By.CSS_SELECTOR, ".tracking-form")
    TRACKING_INPUT = (By.CSS_SELECTOR, "input[name='tracking-number']")
    TRACKING_BUTTON = (By.CSS_SELECTOR, ".tracking-button")
    TRACKING_RESULT = (By.CSS_SELECTOR, ".tracking-result")

    # Элементы для управления заказом
    ORDER_DETAILS = (By.CSS_SELECTOR, ".order-details")
    ORDER_HISTORY = (By.CSS_SELECTOR, ".order-history")
    ORDER_STATUS = (By.CSS_SELECTOR, ".order-status")
    ORDER_CANCEL_BUTTON = (By.CSS_SELECTOR, ".cancel-order-button")
    ORDER_EDIT_BUTTON = (By.CSS_SELECTOR, ".edit-order-button")


class BasePageLocators:
    # Общие элементы
    LOADING_SPINNER = (By.CSS_SELECTOR, ".loading-spinner")
    NOTIFICATION_BAR = (By.CSS_SELECTOR, ".notification-bar")
    PAGE_LOAD_INDICATOR = (By.CSS_SELECTOR, ".loading-indicator")
    PAGE_HEADER = (By.CSS_SELECTOR, ".header")

    # Навигация
    MAIN_MENU = (By.CSS_SELECTOR, ".main-menu")
    MENU_ITEMS = (By.CSS_SELECTOR, ".menu-item")

    # Модальные окна
    MODAL_HEADER = (By.CSS_SELECTOR, ".modal-header")
    MODAL_BODY = (By.CSS_SELECTOR, ".modal-body")
    MODAL_FOOTER = (By.CSS_SELECTOR, ".modal-footer")


class ErrorPageLocators:
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    ERROR_CODE = (By.CSS_SELECTOR, ".error-code")
    RETRY_BUTTON = (By.CSS_SELECTOR, ".retry-button")


class ProfilePageLocators:
    PROFILE_INFO = (By.CSS_SELECTOR, ".profile-info")
    ORDER_HISTORY = (By.CSS_SELECTOR, ".order-history")
    SETTINGS_BUTTON = (By.CSS_SELECTOR, ".settings-button")


class FaqPageLocators:
    # Общие элементы страницы
    FAQ_HEADER = (By.CSS_SELECTOR, ".faq-header")
    SEARCH_FORM = (By.CSS_SELECTOR, ".faq-search-form")
    SORT_OPTIONS = (By.CSS_SELECTOR, ".faq-sort-options")
    QUESTION_LIST = (By.CSS_SELECTOR, ".faq-questions-list")

    # Вопросы и ответы
    QUESTION_ITEMS = (By.CSS_SELECTOR, ".faq-question-item")
    QUESTION_TEXT = (By.CSS_SELECTOR, ".faq-question-item:nth-child({index}) .question-text")
    QUESTION_EXPAND_BUTTON = (By.CSS_SELECTOR, ".faq-question-item:nth-child({index}) .expand-button")
    ANSWER_TEXT = (By.CSS_SELECTOR, ".faq-question-item:nth-child({index}) .answer-text")

    # Сортировка
    SORT_BY = (By.CSS_SELECTOR, ".sort-option[data-sort='{sort_by}']")

    # Поиск
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search-input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-button")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".search-result")

    # Навигация по страницам
    NEXT_PAGE = (By.CSS_SELECTOR, ".next-page-button")
    PREV_PAGE = (By.CSS_SELECTOR, ".prev-page-button")
    CURRENT_PAGE = (By.CSS_SELECTOR, ".current-page")

    # Обратная связь
    FEEDBACK_INPUT = (By.CSS_SELECTOR, ".feedback-input")
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, ".feedback-submit")
    FEEDBACK_SUCCESS = (By.CSS_SELECTOR, ".feedback-success-message")

    # Дополнительные элементы
    FAQ_CATEGORIES = (By.CSS_SELECTOR, ".faq-categories")
    CATEGORY_FILTER = (By.CSS_SELECTOR, ".category-filter[data-category='{category}']")
    LOADING_INDICATOR = (By.CSS_SELECTOR, ".faq-loading-indicator")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".no-results-message")

    # Модальное окно
    MODAL_WINDOW = (By.CSS_SELECTOR, ".faq-modal")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal-close-button")

    # Уведомления
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, ".success-notification")
    ERROR_NOTIFICATION = (By.CSS_SELECTOR, ".error-notification")

    # Избранное
    FAVORITE_BUTTON = (By.CSS_SELECTOR, ".favorite-button")
    FAVORITE_LIST = (By.CSS_SELECTOR, ".favorite-list")

    # Поделиться
    SHARE_BUTTON = (By.CSS_SELECTOR, ".share-button")
    SHARE_MODAL = (By.CSS_SELECTOR, ".share-modal")

    # Печать
    PRINT_BUTTON = (By.CSS_SELECTOR, ".print-button")

    # Настройки отображения
    VIEW_OPTIONS = (By.CSS_SELECTOR, ".view-options")

    # Статистика
    STATISTICS_SECTION = (By.CSS_SELECTOR, ".statistics-section")

    # Языки
    LANGUAGE_SELECTOR = (By.CSS_SELECTOR, ".language-selector")

    # Версии
    VERSION_SELECTOR = (By.CSS_SELECTOR, ".version-selector")
