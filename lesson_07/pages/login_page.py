from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object страницы авторизации магазина."""

    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        self.open_url("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.wait_for(self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_for(self.PASSWORD).send_keys(password)

    def click_login(self):
        self.wait_for_clickable(self.LOGIN_BUTTON).click()
