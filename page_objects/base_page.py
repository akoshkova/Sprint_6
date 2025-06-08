from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.wait = WebDriverWait(browser, timeout)
        self.browser.get(url)

    # Базовые методы работы с элементами
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)


    # Методы работы с действиями
    def hover_over_element(self, element):
        ActionChains(self.browser).move_to_element(element).perform()

    def double_click(self, element):
        ActionChains(self.browser).double_click(element).perform()

    def right_click(self, element):
        ActionChains(self.browser).context_click(element).perform()

    def drag_and_drop(self, source, target):
        ActionChains(self.browser).drag_and_drop(source, target).perform()

    # Методы ожидания
    def wait_for_element_visibility(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_invisibility(self, by, value):
        return self.wait.until(EC.invisibility_of_element_located((by, value)))

    def wait_for_element_clickability(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    # Методы работы с окнами
    def switch_to_window(self, window_index):
        windows = self.browser.window_handles
        if len(windows) > window_index:
            self.browser.switch_to.window(windows[window_index])

    def switch_to_frame(self, frame_ref):
        self.browser.switch_to.frame(frame_ref)

    # Методы работы с текстом
    def get_element_text(self, by, value):
        return self.find_element(by).text

    def get_element_attribute(self, by, value, attribute):
        return self.find_element(by).get_attribute(attribute)

    # Методы работы с кликами
    def click_element(self, by):
        element = self.find_element(by)
        self.browser.execute_script("arguments[0].click();", element)

    def js_click(self, element):
        self.browser.execute_script("arguments[0].click();", element)

    # Методы работы с прокруткой
    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_top(self):
        self.browser.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scroll")
