import pytest
import requests



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
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=payload)
        assert response.status_code == 403
        assert response.json() == {"success": False, "message": "User already exists"}


    def test_create_user_without_password(self):
        payload = {
            "email": "spartak@mail.ru",
            "password": "",
            "name": "spartak"
        }
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=payload)
        assert response.status_code == 403
        assert response.json() == {"success":False,"message":"Email, password and name are required fields"}
