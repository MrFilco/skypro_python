from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def init(self, driver):
        self.driver = driver

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self):
        total_text = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text
        return total_text.split()[-1]