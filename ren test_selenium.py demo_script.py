from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

input("Нажми Enter, чтобы закрыть браузер...")
driver.quit()
