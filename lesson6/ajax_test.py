import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")
    
    # Нажатие на синюю кнопку
    blue_button = driver.find_element(By.ID, "ajaxButton")
    blue_button.click()
    
    # Ожидание появления текста
    driver.implicitly_wait(30)  # Ожидание в течение 30 секунд
    green_label = driver.find_element(By.CSS_SELECTOR, ".bg-success")
    text = green_label.text
    
    # Вывод текста в консоль
    print(text)
finally:
    # Закрытие браузера
    driver.quit()
