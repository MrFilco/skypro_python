from selenium.webdriver.common.by import By

class LoginPage:
    def init(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()