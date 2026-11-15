from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 4


class BasePage:
    """Базовый класс для всех страниц."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def wait_for(self, locator, timeout=DEFAULT_TIMEOUT):
        """Ожидает видимости элемента и возвращает его."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_text(self, locator, text, timeout=DEFAULT_TIMEOUT):
        """Ожидает, что элемент получит заданный текст.

        Возвращает True, если текст появился, и False, если время вышло.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            return True
        except TimeoutException:
            return False
