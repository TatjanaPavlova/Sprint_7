import requests
import pytest
import allure
from data import Url, ResponseMessages, DataForRegistration, CourierData
from generators import generate_random_string


@allure.epic("Курьеры")
@allure.feature("Создание курьера")
class TestCourierCreation:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(8),
            "password": generate_random_string(10),
            "firstName": CourierData.FIRST_NAME
        }
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_CREATE}', json=payload)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title("Ошибка при создании двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        login = generate_random_string(8)
        password = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": CourierData.DUPLICATE_NAME
        }

        requests.post(f'{Url.BASE_URL}{Url.COURIER_CREATE}', json=payload)
        duplicate = requests.post(f'{Url.BASE_URL}{Url.COURIER_CREATE}', json=payload)

        assert duplicate.status_code == 409
        assert ResponseMessages.COURIER_ALREADY_EXISTS in duplicate.json().get("message")

    @allure.title("Ошибка при создании курьера без обязательных полей")
    @pytest.mark.parametrize("data_setup", DataForRegistration.incomplete_data)
    def test_create_courier_missing_required_fields(self, data_setup):
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_CREATE}', json=data_setup)
        assert response.status_code == 400
        assert ResponseMessages.COURIER_NOT_ENOUGH_DATA in response.json().get("message")