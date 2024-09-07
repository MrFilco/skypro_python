# lesson_10/test_patch_employee.py
import requests
import allure
from test_auth import get_token
from test_post_employee import create_employee_via_api
from test_create_company import create_company
from db_utils import SessionLocal, delete_employee, setup_db, teardown_db

BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "Content-Type": "application/json", "accept": "application/json"}

def setup_module(module):
    setup_db()

def teardown_module(module):
    teardown_db()

@allure.title("Обновление данных сотрудника")
@allure.description("Тестирование обновления данных сотрудника")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_employee():
    db = SessionLocal()
    company_id = create_company()

    with allure.step("Создаем сотрудника через API"):
        employee_id = create_employee_via_api(company_id)

    with allure.step("Обновляем сотрудника через API"):
        update_data = {
            "lastName": "NewLastName",
            "email": "newemail@example.com",
            "url": "http://newurl.com",
            "phone": "+1234567890",
            "isActive": True
        }
        response = requests.patch(f"{BASE_URL}{EMPLOYEE_ENDPOINT}/{employee_id}", json=update_data, headers=HEADERS)
        assert response.status_code == 200

        # Добавляем отладочные выводы
        response_data = response.json()
        allure.step(f"Response Data: {response_data}")

        # Получаем обновленную запись
        updated_response = requests.get(f"{BASE_URL}{EMPLOYEE_ENDPOINT}/{employee_id}", headers=HEADERS)
        updated_data = updated_response.json()
        
        # Проверяем наличие ключа и его значение
        assert 'lastName' in updated_data, "Key 'lastName' is missing in response"
        assert updated_data["lastName"] == update_data["lastName"], "Employee last name was not updated correctly"

    with allure.step("Удаляем тестового сотрудника из БД"):
        delete_employee(db, employee_id)
    db.close()
