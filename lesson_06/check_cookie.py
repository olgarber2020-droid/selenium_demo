from selenium import webdriver

BASE_URL = "https://gitflic.ru/"

COOKIES_1 = [
    {
        "name": "domain_sid",
        "value": "N2Wh8n9mDC5mT68lOF_0l%3A1794056214382",
        "domain": ".gitflic.ru",
    },
    {
        "name": "remember-me",
        "value": "S0Z6WmVqczVRcjJvZldSSkx1RDE1dyUzRCUzRDpEbERJQ0JtSDQ4clQ5ZXh0VU13cUdBJTNEJTNE",
        "domain": "gitflic.ru",
    },
    {
        "name": "SESSION",
        "value": "ZWI1ZGFlZTYtZTNiMi00ZmQ4LTgxOTgtYTBmNzA0YjNjOTM0",
        "domain": "gitflic.ru",
    },
]

driver = webdriver.Chrome()
driver.get(BASE_URL)
for c in COOKIES_1:
    driver.add_cookie(c)
driver.refresh()
driver.implicitly_wait(5)

print("Есть 'Выйти':", "Выйти" in driver.page_source)
print("Есть ник olik_1:", "olik_1" in driver.page_source)

input("Нажми Enter, чтобы закрыть браузер...")
driver.quit()
