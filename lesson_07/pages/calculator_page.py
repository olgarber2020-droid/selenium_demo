from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage, DEFAULT_TIMEOUT


class CalculatorPage(BasePage):
    """Page Object страницы slow-calculator."""

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.open_url(
            "https://bonigarcia.dev/selenium-webdriver-java"
            "/slow-calculator.html"
        )

    def set_delay(self, value):
        delay_field = self.wait_for(self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(value))

    def click_button(self, label):
        """Нажимает кнопку калькулятора по её надписи."""
        button = self.wait_for_clickable(
            (By.XPATH, f"//span[contains(@class, 'btn') and text()='{label}']")
        )
        button.click()

    def get_screen_text(self, timeout=4):
        """Читает текст с экрана калькулятора, ожидая его обновления."""
        self.wait_for(self.SCREEN, timeout=timeout)
        return self.driver.find_element(*self.SCREEN).text

    def wait_for_result(self, expected, timeout=DEFAULT_TIMEOUT):
        """Ждёт, пока на экране появится результат, и возвращает его текст."""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self.driver.find_element(*self.SCREEN).text
