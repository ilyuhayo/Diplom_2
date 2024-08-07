import pytest
import requests
from faker import Faker


@pytest.fixture
def user_data():
    faker = Faker()
    payload = {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    }

    yield payload
