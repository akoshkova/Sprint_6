# Sprint_6

## Автоматизация тестирования веб-приложения “Scooter”
Описание проекта

Автоматизированная система тестирования веб-приложения “Scooter” с использованием Python, PyTest и Selenium.

Проект включает в себя тесты для проверки функциональности главной страницы, страницы заказа и страницы успешного оформления заказа.

## Структура проекта
~~~
Sprint_6/
├── README.md
├── conftest.py
├── allure-results/
├── page_objects/
│ ├── base_page.py
│ ├── main_page.py
│ ├── order_page.py
│ ├── locators.py
│ └── faq_page.py
└── tests/
  ├── test_faq.py
  └── test_order.py

~~~

## Требования
* Python 3.8+
* PyTest
* Selenium WebDriver
* ChromeDriver
* Allure TestOps
* PyTest-Allure-Adapter

## Основные компоненты
- глобальный файл с фикстурами
- page_objects - паттерн Page Object для работы с элементами
- tests - директория с тестовыми кейсами
- allure-results - папка для хранения результатов тестирования

## История изменений
* 08.06.2025 - Создание проекта