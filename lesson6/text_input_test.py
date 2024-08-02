from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # Переход на сайт
    driver.get("http://uitestingplayground.com/textinput")
    
    # Ввод текста в поле
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    
    # Нажатие на синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    
    # Получение текста кнопки и вывод в консоль
    updated_button_text = blue_button.text
    print(updated_button_text)
finally:
    # Закрытие браузера
    driver.quit()
