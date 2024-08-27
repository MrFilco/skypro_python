# lesson_8/test_post_employee.py
import requests
from test_auth import get_token
from test_create_company import create_company

BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "Content-Type": "application/json", "accept": "application/json"}

def create_employee(company_id):
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
    company_id = create_company()
    employee_id = create_employee(company_id)
    assert employee_id is not None
