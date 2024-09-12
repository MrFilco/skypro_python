# lesson_9/test_create_company.py
import requests
from test_auth import get_token

BASE_URL = "https://x-clients-be.onrender.com"
COMPANY_ENDPOINT = "/company"
TOKEN = get_token("leyla", "water-fairy")
HEADERS = {"x-client-token": TOKEN, "Content-Type": "application/json", "accept": "application/json"}

def create_company():
    payload = {
        "name": "Fil",
        "description": "Test"
    }
    response = requests.post(f"{BASE_URL}{COMPANY_ENDPOINT}", json=payload, headers=HEADERS)
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
    company_id = response.json()["id"]
    assert company_id is not None, "Failed to create company, no ID returned"
    return company_id

def test_create_company():
    company_id = create_company()
    assert company_id is not None
