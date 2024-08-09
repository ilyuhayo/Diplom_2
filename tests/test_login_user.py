import pytest
import requests


class TestLogin:
    def test_login_user(self, create_user):
        payload_auth = {
            "email": create_user["email"],
            "password": create_user["password"]
        }
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=payload_auth)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True


    def test_login_user_with_invalid_data(self):
        payload = {
            "email": "dyadka@mail.rufalse",
            "password": "123456false"
        }
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=payload)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] == False
        assert response_data["message"] == "email or password are incorrect"


