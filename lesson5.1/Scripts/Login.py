from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def login(driver):
    driver.get("http://the-internet.herokuapp.com/login")
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    username_field.send_keys('tomsmith')
    password_field.send_keys('SuperSecretPassword!')
    login_button.click()
    # Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
login(chrome_driver)
chrome_driver.quit()

# Firefox
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
login(firefox_driver)
firefox_driver.quit()