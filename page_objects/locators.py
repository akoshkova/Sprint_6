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
    # Основной заголовок страницы
    FAQ_HEADER = (By.CSS_SELECTOR, '.faq-header')

    # Вопросы и ответы
    FAQ_QUESTIONS = (By.CSS_SELECTOR, '.faq-question')
    FAQ_ANSWERS = (By.CSS_SELECTOR, '.faq-answer')

    # Поиск
    SEARCH_INPUT = (By.CSS_SELECTOR, '.search-input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.search-button')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.search-result')

    # Сортировка
    SORT_POPULARITY = (By.CSS_SELECTOR, '.sort-popularity')
    SORT_RECENT = (By.CSS_SELECTOR, '.sort-recent')

    # Обратная связь
    FEEDBACK_INPUT = (By.CSS_SELECTOR, '.feedback-input')
    FEEDBACK_BUTTON = (By.CSS_SELECTOR, '.feedback-button')
    FEEDBACK_SUCCESS = (By.CSS_SELECTOR, '.feedback-success')

    # Пагинация
    NEXT_PAGE = (By.CSS_SELECTOR, '.next-page')
    PREVIOUS_PAGE = (By.CSS_SELECTOR, '.previous-page')
    CURRENT_PAGE = (By.CSS_SELECTOR, '.current-page')

    # Общие элементы
    LOADING_SPINNER = (By.CSS_SELECTOR, '.loading-spinner')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message')

    # Дополнительные элементы
    FAQ_CATEGORY = (By.CSS_SELECTOR, '.faq-category')
    FAQ_FILTER = (By.CSS_SELECTOR, '.faq-filter')
    FAQ_SHARE_BUTTON = (By.CSS_SELECTOR, '.faq-share-button')
    FAQ_PRINT_BUTTON = (By.CSS_SELECTOR, '.faq-print-button')

    # Модальные окна
    MODAL_WINDOW = (By.CSS_SELECTOR, '.modal-window')
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '.modal-close-button')

    # Уведомления
    NOTIFICATION_BAR = (By.CSS_SELECTOR, '.notification-bar')
    NOTIFICATION_CLOSE_BUTTON = (By.CSS_SELECTOR, '.notification-close-button')

    # Форма обратной связи
    FEEDBACK_FORM = (By.CSS_SELECTOR, '.feedback-form')
    FEEDBACK_SUBMIT_BUTTON = (By.CSS_SELECTOR, '.feedback-submit-button')
    FEEDBACK_CANCEL_BUTTON = (By.CSS_SELECTOR, '.feedback-cancel-button')

    # Настройки отображения
    VIEW_SETTINGS = (By.CSS_SELECTOR, '.view-settings')
    VIEW_MODE_SWITCH = (By.CSS_SELECTOR, '.view-mode-switch')

    # Избранное
    FAVORITE_BUTTON = (By.CSS_SELECTOR, '.favorite-button')
    FAVORITE_LIST = (By.CSS_SELECTOR, '.favorite-list')

    # Навигация
    NAVIGATION_MENU = (By.CSS_SELECTOR, '.navigation-menu')
    NAVIGATION_ITEM = (By.CSS_SELECTOR, '.navigation-item')

    # Лоадеры для отдельных элементов
    QUESTION_LOADING = (By.CSS_SELECTOR, '.question-loading')
    ANSWER_LOADING = (By.CSS_SELECTOR, '.answer-loading')

    # Специальные элементы
    ACCESSIBILITY_HINT = (By.CSS_SELECTOR, '.accessibility-hint')
    SCREEN_READER_ONLY = (By.CSS_SELECTOR, '.screen-reader-only')
