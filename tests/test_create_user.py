import pytest
import requests



class TestCreateUser:
    def test_create_user(self, user_data):
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=user_data)
        response_data = response.json()
        assert response.status_code == 200
        assert "email" in response_data["user"]
        assert "name" in response_data["user"]
        assert "accessToken" in response_data
        assert "refreshToken" in response_data


        access_token = response_data["accessToken"]
        response = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user",
                                   headers={'Authorization': f"{access_token}"})
        assert response.status_code == 202


    def test_create_identical_user(self):
        payload = {
            "email": "dyadka@mail.ru",
            "password": "123456",
            "name": "dyadka"
        }
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=payload)
        assert response.status_code == 403
        assert response.json() == {"success": False, "message": "User already exists"}


    def test_create_user_without_password(self):
        payload = {
            "email": "spartak@mail.ru",
            "password": "",
            "name": "spartak"
        }
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=payload)
        assert response.status_code == 403
        assert response.json() == {"success":False,"message":"Email, password and name are required fields"}
