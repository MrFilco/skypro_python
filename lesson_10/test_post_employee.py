# lesson_10/test_post_employee.py
import requests
import allure
from test_auth import get_token
from test_create_company import create_company
from db_utils import SessionLocal, delete_employee, setup_db, teardown_db, Employee

BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "Content-Type": "application/json", "accept": "application/json"}

def setup_module(module):
    setup_db()

def teardown_module(module):
    teardown_db()

def create_employee_via_api(company_id: int) -> int:
    """
    Создает сотрудника через API.
    
    :param company_id: ID компании, в которой работает сотрудник.
    :return: ID созданного сотрудника.
    """
    payload = {
        "firstName": "Andy",
        "lastName": "Fil",
        "middleName": "AF",
        "companyId": company_id,
        "email": "filtestqa@mail.ru",
        "url": "string",
        "phone": "+78968887766",
        "birthdate": "2024-08-27T08:47:06.328Z",
        "isActive": True
    }
    response = requests.post(f"{BASE_URL}{EMPLOYEE_ENDPOINT}", json=payload, headers=HEADERS)
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
    employee_id = response.json()["id"]
    assert employee_id is not None, "Failed to create employee, no ID returned"
    return employee_id

@allure.title("Создание сотрудника")
@allure.description("Тестирование создания нового сотрудника")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_post_employee():
    db = SessionLocal()
    company_id = create_company()

    with allure.step("Создаем сотрудника через API"):
        employee_id = create_employee_via_api(company_id)

    with allure.step("Проверяем, что сотрудник добавлен в БД"):
        created_employee = db.query(Employee).filter(Employee.id == employee_id).first()
        assert created_employee is not None, "Employee not found in the database"

    with allure.step("Удаляем тестового сотрудника из БД"):
        delete_employee(db, employee_id)
    db.close()
