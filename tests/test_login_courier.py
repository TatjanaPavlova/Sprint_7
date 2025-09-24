import requests
import allure
from data import Url, ResponseMessages
from generators import generate_random_string


@allure.epic("Курьеры")
@allure.feature("Логин курьера")
class TestCourierLogin:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, create_courier):
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=create_courier[1])
        courier_id = response.json().get("id")
        assert response.status_code == 200
        assert courier_id is not None

    @allure.title("Ошибка при логине несуществующего курьера")
    def test_login_unregistered_courier(self):
        login_data = {
            "login": generate_random_string(8),
            "password": generate_random_string(10)
        }
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_data)
        assert response.status_code == 404
        assert ResponseMessages.COURIER_NOT_FOUND in response.json().get("message")

    @allure.title("Ошибка при логине без пароля")
    def test_login_without_password(self, create_courier):
        login_data = {"login": create_courier[2], "password": ""}
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_data)
        assert response.status_code == 400
        assert ResponseMessages.COURIER_LOGIN_NOT_ENOUGH_DATA in response.json().get("message")

    @allure.title("Ошибка при логине без логина")
    def test_login_without_login(self, create_courier):
        login_data = {"login": "", "password": create_courier[3]}
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_data)
        assert response.status_code == 400
        assert ResponseMessages.COURIER_LOGIN_NOT_ENOUGH_DATA in response.json().get("message")
