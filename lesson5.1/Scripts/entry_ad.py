from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def input_text(driver):
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_field = driver.find_element(By.TAG_NAME, 'input')
    input_field.send_keys('1000')
    input_field.clear()
    input_field.send_keys('999')

# Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
input_text(chrome_driver)
chrome_driver.quit()

# Firefox
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
input_text(firefox_driver)
firefox_driver.quit()
