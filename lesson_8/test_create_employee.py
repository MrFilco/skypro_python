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

def test_get_companies(auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{BASE_URL}/company", headers=headers)
    print(response.status_code)
    companies = response.json()
    print(companies)  # Вывод списка компаний
    assert response.status_code == 200

    # Сохраните IDs компаний для последующего использования
    # Например, вы можете записать их в файл или использовать как глобальные переменные
    # Например, сохраните в файл для дальнейшего использования
    with open('company_ids.json', 'w') as f:
        import json
        json.dump(companies, f)
