from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_yougile_login():
    driver = webdriver.Chrome()
    # Открыть страницу авторизации: https://ru.yougile.com/team/
    driver.get("https://ru.yougile.com/team/")
    driver.maximize_window()
    sleep(2)

    # Ввести логин в поле «Email» sky-best-student@yandex.ru [autocomplete="email"]
    driver.find_element(By.CSS_SELECTOR, "[autocomplete='email']").send_keys(
        "sky-best-student@yandex.ru"
    )

    # Ввести пароль в поле «Пароль» Sky_Pro1 [autocomplete="current-password"]
    driver.find_element(By.CSS_SELECTOR, "[autocomplete='current-password']").send_keys(
        "Sky_Pro1"
    )

    # Нажать кнопку «Войти». bg-action-default[role="button"]
    driver.find_element(
        By.CSS_SELECTOR, ".bg-action-default[role='button']").click()

    # Ждем загрузки страницы после логина
    sleep(5)

    # Переход на страницу настроек аккаунта
    driver.get("https://ru.yougile.com/team/settings-account")
    sleep(5)

    # Проверяем, что отображается имя пользователя
    user_name = driver.find_element(By.CSS_SELECTOR, "[placeholder='Отображаемое имя…']")
    assert user_name.is_displayed()
    assert user_name.get_attribute("value") == "Sky_Pro"

    driver.quit()