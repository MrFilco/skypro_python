# lesson_8/test_get_employees.py
import requests
from test_auth import get_token
from test_create_company import create_company

BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "accept": "application/json"}

def test_get_employees():
    company_id = create_company()
    response = requests.get(f"{BASE_URL}{EMPLOYEE_ENDPOINT}?company={company_id}", headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list), "Expected response to be a list of employees"
