# lesson_10/test_auth.py
import requests
import allure

BASE_URL = "https://x-clients-be.onrender.com"
AUTH_ENDPOINT = "/auth/login"

def get_token(username: str, password: str) -> str:
    """
    Получает токен для авторизации.
    
    :param username: Имя пользователя.
    :param password: Пароль.
    :return: Токен авторизации.
    """
    response = requests.post(
        f"{BASE_URL}{AUTH_ENDPOINT}",
        json={"username": username, "password": password}
    )
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
    return response.json()['userToken']

@allure.title("Получение токена")
@allure.description("Тестирование получения токена для авторизации")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_token():
    with allure.step("Получаем токен для авторизации"):
        token = get_token("leyla", "water-fairy")
        assert token is not None
