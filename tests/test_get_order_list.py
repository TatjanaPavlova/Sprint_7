import requests
import allure
from data import Url, Flags


@allure.epic("Заказы")
@allure.feature("Список заказов")
class TestOrderList:

    @allure.title("Получение списка заказов")
    def test_get_order_list_success(self):
        response = requests.get(f'{Url.BASE_URL}{Url.GET_ORDER_LIST}')
        assert response.status_code == 200
        assert Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()