import pytest
import requests

BASE_URL = "https://x-clients-be.onrender.com"

@pytest.fixture
def auth_token():
    return auth_token()

def test_get_employees(auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{BASE_URL}/employee", headers=headers)
    print(response.status_code)
    print(response.text)  # Вывод тела ответа для отладки
    assert response.status_code == 200

