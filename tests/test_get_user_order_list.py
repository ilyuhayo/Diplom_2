import allure
import pytest
import requests
from responses_text import RESPONSES_TEXT
from urls import API_URLS


class TestGetUserOrderList:
    @allure.title("Получение списка заказов пользователя с авторизацией")
    def test_get_user_oder_with_auth(self, create_user_and_order):
        user_info = create_user_and_order
        headers = {"Authorization": user_info["accessToken"]}
        response = requests.get(API_URLS.ORDER_ENDPOINT, headers=headers)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True


    @allure.title("Получение списка заказов пользователя без авторизации")
    def test_get_user_oder_without_auth(self):
        response = requests.get(API_URLS.ORDER_ENDPOINT)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] == False
        assert response_data["message"] == RESPONSES_TEXT.UNAUTHORISED_ERROR
