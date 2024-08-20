# lesson7/page_objects/login_page.py

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver  # Инициализация WebDriver в классе

    def load(self):
        self.driver.get("https://www.saucedemo.com/")  # Загрузка страницы входа

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
