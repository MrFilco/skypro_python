import requests
import pytest

BASE_URL = "https://x-clients-be.onrender.com"

@pytest.fixture
def auth_token():
    url = f"{BASE_URL}/auth/login"
    credentials = {
        "username": "raphael",
        "password": "cool-but-crude"
    }
    response = requests.post(url, json=credentials)
    assert response.status_code == 201
    return response.json()['userToken']

@pytest.fixture
def employee_id():
    # Убедитесь, что у вас есть ID сотрудника для этого теста
    return 1  # Замените на действительный ID сотрудника

def test_patch_employee(auth_token, employee_id):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    patch_data = {
        "lastName": "Doe",
        "email": "new.email@example.com",
        "url": "http://newexample.com",
        "phone": "0987654321",
        "isActive": True
    }
    response = requests.patch(f"{BASE_URL}/employee/{employee_id}", headers=headers, json=patch_data)
    print(response.status_code)
    print(response.text)  # Вывод для отладки
    assert response.status_code == 201
