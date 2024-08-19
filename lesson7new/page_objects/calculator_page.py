from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    
    def load(self):
        self.driver.get(self.url)

    def set_delay(self, delay_value):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def press_buttons(self, buttons):
        for button in buttons:
            button_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))
            )
            button_element.click()

    def wait_for_result(self, result_text):
        WebDriverWait(self.driver, 70).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), result_text)
        )

    def get_screen_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.screen").text.strip()
