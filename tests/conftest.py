import pytest
import requests
from faker import Faker
from urls import API_URLS


@pytest.fixture()
def user_data():
    faker = Faker()
    return {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    }


@pytest.fixture()
def create_user(user_data):
    payload = user_data
    response_post = requests.post(API_URLS.REGISTER_USER_ENDPOINT, json=payload)
    response_data = response_post.json()
    user_info = {
        "email": response_data['user']['email'],
        "name": response_data['user']['name'],
        "password": payload["password"],
        "accessToken": response_data["accessToken"],
        "refreshToken": response_data["refreshToken"]
    }
    yield user_info

    headers = {
        'Authorization': f"Bearer {user_info['accessToken']}"
    }
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)


@pytest.fixture()
def create_user_with_auth(create_user):
    user_info = create_user

    payload_auth = {
        "email": user_info['email'],
        "password": user_info['password']
    }
    response_post_auth = requests.post(API_URLS.LOGIN_USER_ENDPOINT, json=payload_auth)
    auth_data = response_post_auth.json()

    user_info["accessToken"] = auth_data["accessToken"]
    user_info["refreshToken"] = auth_data["refreshToken"]

    yield user_info

    headers = {
        'Authorization': f"Bearer {user_info['accessToken']}"
    }
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)


@pytest.fixture()
def create_user_and_order(create_user_with_auth):
    user_info = create_user_with_auth

    headers = {"Authorization": user_info["accessToken"]}
    order_payload = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa72"
        ]
    }
    response_create_order = requests.post(API_URLS.ORDER_ENDPOINT,
                                          json=order_payload, headers=headers)
    order_data = response_create_order.json()

    user_info["order_id"] = order_data["order"]["number"]

    yield user_info

    headers = {"Authorization": user_info["accessToken"]}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)
