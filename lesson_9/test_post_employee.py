# lesson_9/test_post_employee.py
import requests
from test_auth import get_token
from test_create_company import create_company
from db_utils import SessionLocal, delete_employee, setup_db, teardown_db, Employee

BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "Content-Type": "application/json", "accept": "application/json"}

def setup_module(module):
    """Setup any state specific to the execution of the given module."""
    setup_db()

def teardown_module(module):
    """Teardown any state that was previously setup with a setup_module method."""
    teardown_db()

def create_employee_via_api(company_id):
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

def test_post_employee():
    db = SessionLocal()
    company_id = create_company()

    # Создаем сотрудника через API
    employee_id = create_employee_via_api(company_id)

    # Проверяем, что сотрудник добавлен в БД
    created_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    assert created_employee is not None, "Employee not found in the database"

    # Удаляем тестового сотрудника из БД после теста
    delete_employee(db, employee_id)
    db.close()
