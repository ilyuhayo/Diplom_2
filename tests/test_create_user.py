import pytest
import requests
from responses_text import RESPONSES_TEXT
from urls import API_URLS


class TestCreateUser:
    def test_create_user(self, create_user):
        assert create_user["accessToken"] is not None
        assert create_user["refreshToken"] is not None


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

