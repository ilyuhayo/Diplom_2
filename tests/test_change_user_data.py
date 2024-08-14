import allure
import pytest
import requests
from faker import Faker
from responses_text import RESPONSES_TEXT
from urls import API_URLS

class TestChangeUserData:
    @allure.title("Изменение данных пользователя")
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
            API_URLS.USER_ENDPOINT,
            json=payload,
            headers=headers
        )
        response_patch_data = response_patch.json()
        assert response_patch.status_code == 200
        assert response_patch_data['success'] == True


    @allure.title("Изменение данных пользователя без авторизации")
    def test_change_user_data_without_auth(self, create_user):
        faker = Faker()
        payload = {
            "email": faker.email(),
            "password": faker.password()
        }
        response_patch = requests.patch(API_URLS.USER_ENDPOINT, json=payload)
        response_patch_data = response_patch.json()
        assert response_patch.status_code == 401
        assert response_patch_data["message"] == RESPONSES_TEXT.UNAUTHORISED_ERROR
