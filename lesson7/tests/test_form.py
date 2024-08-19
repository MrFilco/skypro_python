import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.form_page import FormPage
   


@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def test_form_submission(driver):
    form_page = FormPage(driver)
    form_page.load()

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    
    form_page.fill_form_fields(form_data)
    form_page.click_submit()

    for field_name in form_data.keys():
        form_page.validate_field_success(field_name)

    form_page.validate_field_error("zip-code")