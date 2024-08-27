import requests
from test_auth import get_token
from test_post_employee import create_employee
from test_create_company import create_company
BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "accept": "application/json"}

def test_get_employee_by_id():
    company_id = create_company()
    employee_id = create_employee(company_id)
    
    response = requests.get(f"{BASE_URL}{EMPLOYEE_ENDPOINT}/{employee_id}", headers=HEADERS)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == employee_id, "Employee ID does not match"