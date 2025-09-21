import requests
import pytest
import allure
from data import Url, Flags, DataForOrder


@allure.epic("Заказы")
@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Создание заказа с разными вариантами цветов")
    @pytest.mark.parametrize("scooter_color", DataForOrder.scooter_color)
    def test_create_order_with_colors(self, scooter_color):
        order_data = DataForOrder.order_data.copy()
        order_data["color"] = scooter_color

        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', json=order_data)
        assert response.status_code == 201
        assert Flags.SUCCESSFUL_ORDER_CREATION in response.json()

        # отменяем заказ, чтобы удалить тестовые данные
        track = response.json()["track"]
        requests.put(f'{Url.BASE_URL}{Url.CANCEL_ORDER}', params={"track": track})