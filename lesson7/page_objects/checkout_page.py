# lesson7/page_objects/checkout_page.py

from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver  # Инициализация WebDriver в классе

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
