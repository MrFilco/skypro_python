from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
       def __init__(self, driver):
           self.driver = driver
           self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

       def load(self):
           self.driver.get(self.url)

       def fill_form(self, form_data):
           for field_name, value in form_data.items():
               field = WebDriverWait(self.driver, 10).until(
                   EC.visibility_of_element_located((By.NAME, field_name))
               )
               field.send_keys(value)

       def submit(self):
           submit_button = WebDriverWait(self.driver, 10).until(
               EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
           )
           submit_button.click()

       def validate_field_success(self, field_name):
           field = WebDriverWait(self.driver, 10).until(
               EC.visibility_of_element_located((By.ID, field_name))
           )
           assert "alert-success" in field.get_attribute("class").split(), f"Поле '{field_name}' должно быть подсвечено зеленым."

       def validate_field_error(self, field_id):
           field = WebDriverWait(self.driver, 10).until(
               EC.visibility_of_element_located((By.ID, field_id))
           )
           assert "alert-danger" in field.get_attribute("class").split(), f"Поле '{field_id}' должно быть подсвечено красным."
   
