import requests
import pytest
from data import Url
from generators import generate_random_string

@pytest.fixture
def create_courier():
    """Создаёт нового курьера перед тестом и удаляет после теста"""
    login = generate_random_string(8)
    password = generate_random_string(10)
    first_name = generate_random_string(6)

    create_body = {"login": login, "password": password, "firstName": first_name}
    login_body = {"login": login, "password": password}

    # Регистрируем курьера
    requests.post(f'{Url.BASE_URL}{Url.COURIER_CREATE}', json=create_body)
    login_response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_body)

    yield [create_body, login_body, login, password]

    # Удаляем курьера после теста, если ID получен
    courier_id = login_response.json().get("id")
    if courier_id:
        requests.delete(f'{Url.BASE_URL}{Url.COURIER_DELETE}{courier_id}')


@pytest.fixture
def generate_courier_data():
    """Генерирует данные для нового курьера без регистрации"""
    login = generate_random_string(8)
    password = generate_random_string(10)
    first_name = generate_random_string(6)

    create_body = {"login": login, "password": password, "firstName": first_name}
    login_body = {"login": login, "password": password}

    yield [create_body, login_body]

    # Удаляем курьера, если он был создан во время теста
    login_response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_body)
    courier_id = login_response.json().get("id")
    if courier_id:
        requests.delete(f'{Url.BASE_URL}{Url.COURIER_DELETE}{courier_id}')