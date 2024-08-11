import pytest
import requests
from faker import Faker


@pytest.fixture()
def user_data():
    faker = Faker()
    payload = {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    }

    yield payload

@pytest.fixture()
def create_user():
    faker = Faker()
    payload = {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    }
    response_post = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=payload)
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
    response_delete = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

@pytest.fixture()
def create_user_with_auth():
    faker = Faker()
    payload = {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    }
    response_post = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=payload)
    response_data = response_post.json()
    user_info = {
        "email": response_data['user']['email'],
        "name": response_data['user']['name'],
        "password": payload["password"],
        "accessToken": response_data["accessToken"],
        "refreshToken": response_data["refreshToken"]
    }

    payload_auth = {
        "email": response_data['user']['email'],
        "password": payload["password"]
    }
    response_post_auth = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=payload_auth)

    yield user_info

    headers = {
        'Authorization': f"Bearer {user_info['accessToken']}"
    }
    response_delete = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)


@pytest.fixture()
def create_user_and_order():
    faker = Faker()
    payload = {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    }
    response_register = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=payload)
    user_data_info = response_register.json()

    user_info = {
        "email": user_data_info['user']['email'],
        "password": payload['password'],
        "accessToken": user_data_info['accessToken'],
        "refreshToken": user_data_info['refreshToken']
    }

    payload_auth = {
        "email": user_info['email'],
        "password": user_info['password']
    }
    response_login = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=payload_auth)
    auth_data = response_login.json()

    user_info["accessToken"] = auth_data["accessToken"]
    user_info["refreshToken"] = auth_data["refreshToken"]

    headers = {"Authorization": user_info["accessToken"]}
    order_payload = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa72"
        ]
    }
    response_create_order = requests.post("https://stellarburgers.nomoreparties.site/api/orders",
                                          json=order_payload, headers=headers)

    order_data = response_create_order.json()

    user_info["order_id"] = order_data["order"]["number"]

    yield user_info


    headers = {"Authorization": user_info["accessToken"]}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)
