import time
from selenium import webdriver


# Современный способ. Selenium Manager автоматически настроит драйвер
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

# Открываем страницу
driver.get("https://www.google.com")

print(driver.title)
print(driver.current_url)

driver.refresh()

# Ждем 5 секунд (чтобы увидеть результат)
time.sleep(2)

# Закрываем браузер
driver.quit()