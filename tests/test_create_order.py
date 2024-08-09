import pytest
import requests


class TestCreateOrder:
    def test_create_order_by_auth_user(self, create_user_with_auth):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa73"]
        }
        response_post = requests.post("https://stellarburgers.nomoreparties.site/api/orders", json=payload)
        response_post_data = response_post.json()
        assert response_post.status_code == 200
        assert response_post_data["success"] == True
        assert response_post_data["name"] == "Space метеоритный флюоресцентный бургер"


    def test_create_order_by_not_auth_user(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]
        }
        response_post = requests.post("https://stellarburgers.nomoreparties.site/api/orders", json=payload)
        response_post_data = response_post.json()
        assert response_post.status_code == 200
        assert response_post_data["success"] == True
        assert response_post_data["name"] == "Био-марсианский флюоресцентный бургер"


    def test_create_order_without_ingredients(self, create_user_with_auth):
        payload = {
            "ingredients": ""
        }
        response_post = requests.post("https://stellarburgers.nomoreparties.site/api/orders", json=payload)
        response_post_data = response_post.json()
        assert response_post.status_code == 400
        assert response_post_data["success"] == False
        assert response_post_data["message"] == "Ingredient ids must be provided"


    def test_create_order_with_invalid_ingredients(self, create_user_with_auth):
        payload = {
            "ingredients": ["d1f82001bdaaa6d", "01bdaaa70", "61c0c5a71d1f82001b"]
        }
        response_post = requests.post("https://stellarburgers.nomoreparties.site/api/orders", json=payload)
        assert response_post.status_code == 500