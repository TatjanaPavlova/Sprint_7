from generators import generate_random_string

class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru' # главная страница Яндекс Самокат
    COURIER_CREATE = '/api/v1/courier' # создание курьера
    COURIER_LOGIN = '/api/v1/courier/login' # логин курьера в системе
    COURIER_DELETE = '/api/v1/courier/' # удаление курьера (+ id)
    CREATE_ORDER = '/api/v1/orders' # создание заказа
    GET_ORDER_LIST = '/api/v1/orders' # получение списка заказов
    CANCEL_ORDER = '/api/v1/orders/cancel' # отмена заказа (+ params track)
    TRACK_ORDER = '/api/v1/orders/track?t=' # получение заказа по номеру (+ params track)


class CourierData:
    FIRST_NAME = "Ivan"
    DUPLICATE_NAME = "Alex"
    DEFAULT_PASSWORD = "123456"


class DataForOrder:
    order_data = {
        "firstName": "Daria",
        "lastName": "Gavrilova",
        "address": "Voznesenskiy per., 18",
        "metroStation": 4,
        "phone": "+79064568142",
        "rentTime": 2,
        "deliveryDate": "2025-09-26",
        "comment": "домофон не работает"
    }
    scooter_color = [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],   # оба цвета
        []                   # вариант "не указывать цвет"
    ]


class DataForRegistration:
    # набор JSON с отсутствующими обязательными полями для проверки ошибки 400
    incomplete_data = [
        {"password": generate_random_string(8)},   # нет login
        {"login": generate_random_string(8)}       # нет password
    ]


class ResponseMessages:
    COURIER_ALREADY_EXISTS = 'Этот логин уже используется'
    COURIER_NOT_ENOUGH_DATA = 'Недостаточно данных для создания учетной записи'
    COURIER_NOT_FOUND = 'Учетная запись не найдена'
    COURIER_LOGIN_NOT_ENOUGH_DATA = 'Недостаточно данных для входа'


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'