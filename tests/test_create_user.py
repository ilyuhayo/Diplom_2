import allure
import pytest
import requests
from responses_text import RESPONSES_TEXT
from urls import API_URLS


class TestCreateUser:
    @allure.title("Создание пользователя")
    def test_create_user(self, user_data):
        payload = {
            "email": user_data["email"],
            "password": user_data["password"],
            "name": user_data["name"]
        }
        response = requests.post(API_URLS.REGISTER_USER_ENDPOINT, json=payload)
        response_data = response.json()
        assert response.status_code == 200

        headers = {
            'Authorization': f"Bearer {response_data['accessToken']}"
        }
        requests.delete(API_URLS.USER_ENDPOINT, headers=headers)


    @allure.title("Создание существующего пользователя")
    def test_create_identical_user(self):
        payload = {
            "email": "dyadka@mail.ru",
            "password": "123456",
            "name": "dyadka"
        }
        response = requests.post(API_URLS.REGISTER_USER_ENDPOINT, json=payload)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data["success"] == False
        assert response_data["message"] == RESPONSES_TEXT.EXISTING_USER_ERROR


    @allure.title("Создание пользователя без пароля")
    def test_create_user_without_password(self):
        payload = {
            "email": "spartak@mail.ru",
            "password": "",
            "name": "spartak"
        }
        response = requests.post(API_URLS.REGISTER_USER_ENDPOINT, json=payload)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data["success"] == False
        assert response_data["message"] == RESPONSES_TEXT.REQUIRED_PASSWORD_AND_NAME_ERROR

