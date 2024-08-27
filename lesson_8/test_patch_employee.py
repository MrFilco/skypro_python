import requests
from test_auth import get_token
from test_post_employee import create_employee
from test_create_company import create_company

BASE_URL = "https://x-clients-be.onrender.com"
EMPLOYEE_ENDPOINT = "/employee"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "Content-Type": "application/json", "accept": "application/json"}

def test_patch_employee():
    company_id = create_company()
    employee_id = create_employee(company_id)
    
    update_data = {
        "lastName": "NewLastName",
        "email": "newemail@example.com",
        "url": "http://newurl.com",
        "phone": "+1234567890",
        "isActive": True
    }
    response = requests.patch(f"{BASE_URL}{EMPLOYEE_ENDPOINT}/{employee_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 200
    response_data = response.json()
    