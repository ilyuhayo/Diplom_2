import pytest
import requests


class TestGetUserOrderList:
    def test_get_user_oder_with_auth(self, create_user_and_order):
        user_info = create_user_and_order
        headers = {"Authorization": user_info["accessToken"]}
        response = requests.get("https://stellarburgers.nomoreparties.site/api/orders", headers=headers)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True


    def test_get_user_oder_without_auth(self):
        response = requests.get("https://stellarburgers.nomoreparties.site/api/orders")
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] == False
        assert response_data["message"] == "You should be authorised"