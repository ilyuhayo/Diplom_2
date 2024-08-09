import pytest
import requests
from faker import Faker

class TestChangeUserData:
    def test_change_user_data(self, create_user):
        access_token = create_user["accessToken"]
        faker = Faker()
        payload = {
            "email": faker.email(),
            "password": faker.password()
        }

        headers = {
            'Authorization': access_token
        }

        response_patch = requests.patch(
            "https://stellarburgers.nomoreparties.site/api/auth/user",
            json=payload,
            headers=headers
        )
        response_patch_data = response_patch.json()
        assert response_patch.status_code == 200
        assert response_patch_data['success'] == True


    def test_change_user_data_without_auth(self, create_user):
        faker = Faker()
        payload = {
            "email": faker.email(),
            "password": faker.password()
        }
        response_patch = requests.patch("https://stellarburgers.nomoreparties.site/api/auth/user", json=payload)
        response_patch_data = response_patch.json()
        assert response_patch.status_code == 401
        assert response_patch_data == {"success": False, "message": "You should be authorised"}