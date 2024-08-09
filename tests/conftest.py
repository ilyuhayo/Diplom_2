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
    response_post = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=payload)
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
