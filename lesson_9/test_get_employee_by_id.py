# lesson_9/test_get_employee_by_id.py
import requests
from test_auth import get_token
from test_post_employee import create_employee_via_api
from test_create_company import create_company
from db_utils import SessionLocal, delete_employee, setup_db, teardown_db

BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "accept": "application/json"}

def setup_module(module):
    """Setup any state specific to the execution of the given module."""
    setup_db()

def teardown_module(module):
    """Teardown any state that was previously setup with a setup_module method."""
    teardown_db()

def test_get_employee_by_id():
    db = SessionLocal()
    company_id = create_company()

    # Создаем сотрудника через API
    employee_id = create_employee_via_api(company_id)

    # Получаем сотрудника по ID через API
    response = requests.get(f"{BASE_URL}{EMPLOYEE_ENDPOINT}/{employee_id}", headers=HEADERS)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == employee_id, "Employee ID does not match"

    # Удаляем тестового сотрудника из БД после теста
    delete_employee(db, employee_id)
    db.close()
