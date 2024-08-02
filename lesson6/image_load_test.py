from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # Переход на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ожидание загрузки всех картинок
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='Done!']"))
    )
    
    # Получение значения атрибута src у 3-й картинки
    third_image = driver.find_element(By.XPATH, "(//img)[3]")
    src_value = third_image.get_attribute("src")
    
    # Вывод значения в консоль
    print(src_value)
finally:
    # Закрытие браузера
    driver.quit()
