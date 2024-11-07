from http.client import responses

import configuration
import requests
import data
from data import order_body


# Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_CREATE,
                         json=body)

a = create_order(order_body)
#print("Номер заказа", a.json())

# Получение заказа по треку заказа

def get_order(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_NUMBER,
                        params = {'t': track_id})

b = get_order(a.json()["track"])
#print("Данные заказа", b.json())
#print("Код ответа", b.status_code)

#Проверка, что код ответа равен 200
def positive_assert_order_creation():
    create_order_response = create_order(order_body)
    assert create_order_response.status_code == 201, "Ошибка при создании заказа"
    track_id = create_order_response.json().get("track")
    assert track_id is not None, "Трек заказа не получен"
    print("Заказ успешно создан, трек:", track_id)
    get_order_response = get_order(track_id)
    assert get_order_response.status_code == 200, "Ошибка при получении заказа"
    print("Заказ успешно получен с кодом 200")

positive_assert_order_creation()