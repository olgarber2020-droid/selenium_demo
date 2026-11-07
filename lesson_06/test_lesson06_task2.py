from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://gitflic.ru/"

NICK_1 = "olik_1"
NICK_2 = "olik_2"

PROFILE_URL_1 = f"https://gitflic.ru/user/{NICK_1}"
PROFILE_URL_2 = f"https://gitflic.ru/user/{NICK_2}"

COOKIES_1 = [
    {
        "name": "domain_sid",
        "value": "N2Wh8n9mDC5mT68lOF_0l%3A1794056214382",
        "domain": ".gitflic.ru",
    },
    {
        "name": "remember-me",
        "value": "WDlEckslMkZROW1OUm12SEdLSHJpZlJBJTNEJTNEOnE2bDM0N2RxdnlmZjY4SWFGOUVUWEElM0QlM0Q",
        "domain": "gitflic.ru",
    },
    {
        "name": "SESSION",
        "value": "MjFjMmQ1ZGUtOTU2My00MDdjLTlkMmYtMjliZDA2NTlmNjE4",
        "domain": "gitflic.ru",
    },
]

COOKIES_2 = [
    {
        "name": "domain_sid",
        "value": "8yKCco4O-U5FyjDr-hZhI%3A1794073572526",
        "domain": ".gitflic.ru",
    },
    {
            "name": "remember-me",
            "value": "QnZyUzdDbUJSSTZ6OUxPTmklMkY3Z0xRJTNEJTNEOlRacUVRTFNOUTlRU2lrWUdNZ1ZyNkElM0QlM0Q",
            "domain": "gitflic.ru",
    },
    {
        "name": "SESSION",
        "value": "YTkxMWExOTctMDE4Yy00NzdkLTkzY2ItYTBhYzMyODg4YThl",
        "domain": "gitflic.ru",
    },
]


def _login_by_cookie(driver, cookies, username_text):
    """Ставит cookie пользователя, обновляет страницу и ждёт его ника."""
    driver.get(BASE_URL)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//body[contains(., '{username_text}')]")
    ))


def test_session_storage_auth():
    driver = webdriver.Chrome()
    try:
        # Пользователь 1: авторизация через cookie и переход в профиль
        _login_by_cookie(driver, COOKIES_1, NICK_1)
        driver.get(PROFILE_URL_1)
        url_user1 = driver.current_url

        # Разлогин: очистка cookie
        driver.delete_all_cookies()

        # Пользователь 2: авторизация через cookie и переход в профиль
        _login_by_cookie(driver, COOKIES_2, NICK_2)
        driver.get(PROFILE_URL_2)
        url_user2 = driver.current_url

        # URL профилей должны различаться
        assert url_user1 != url_user2, "URL профилей пользователей совпадают"
    finally:
        driver.quit()
