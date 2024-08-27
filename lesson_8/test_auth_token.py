import pytest
import requests

BASE_URL = "https://x-clients-be.onrender.com"

@pytest.fixture
def auth_token():
    credentials = {
        "username": "raphael",
        "password": "cool-but-crude"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=credentials)
    assert response.status_code == 201
    return response.json()['userToken']

def test_get_employees(auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    params = {
        "company": 1  # Замените 1 на существующий id компании
    }
    response = requests.get(f"{BASE_URL}/employee", headers=headers, params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

