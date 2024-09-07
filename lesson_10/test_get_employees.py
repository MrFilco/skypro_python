# lesson_10/test_get_employees.py
import requests
import allure
from test_auth import get_token
from test_create_company import create_company
from db_utils import SessionLocal, create_employee, delete_employee, setup_db, teardown_db

BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "accept": "application/json"}

def setup_module(module):
    setup_db()

def teardown_module(module):
    teardown_db()

@allure.title("Получение сотрудников")
@allure.description("Тестирование получения списка сотрудников")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.NORMAL)
def test_get_employees():
    db = SessionLocal()
    company_id = create_company()

    with allure.step("Создаем тестового сотрудника в БД"):
        employee = create_employee(db, first_name="Test", last_name="Employee", phone="1234567890", email="test@example.com", company_id=company_id)

    with allure.step("Выполняем запрос к API"):
        response = requests.get(f"{BASE_URL}{EMPLOYEE_ENDPOINT}?company={company_id}", headers=HEADERS)
        assert response.status_code == 200
        assert isinstance(response.json(), list), "Expected response to be a list of employees"

    with allure.step("Удаляем тестового сотрудника из БД"):
        delete_employee(db, employee.id)
    db.close()
