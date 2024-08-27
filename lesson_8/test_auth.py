# lesson_8/test_auth.py
import requests

BASE_URL = "https://x-clients-be.onrender.com"
AUTH_ENDPOINT = "/auth/login"

def get_token(username, password):
    response = requests.post(
        f"{BASE_URL}{AUTH_ENDPOINT}",
        json={"username": username, "password": password}
    )
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
    return response.json()['userToken']

def test_get_token():
    token = get_token("leyla", "water-fairy")
    assert token is not None
