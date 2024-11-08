﻿## Долганова Елизавета 23-я когорта 
Инженер по тестированию плюс 
Финальный проект

## Автоматизация теста к API
Этот проект содержит автотесты для проверки функциональности создания и получения заказа по трек-номеру с использованием API.
Структура проекта
- configuration.py — файл с конфигурацией, содержит базовый URL API и пути для создания и получения заказа.
- data.py — файл с данными, содержит тело запроса `order_body` для создания нового заказа.
- test_order.py — основной файл с функциями и автотестом для проверки API.

1. def create_order()
   - Отправляет POST-запрос для создания заказа.
   - Проверяет, что в ответе содержится `track_id` (идентификатор заказа).
   - Возвращает `track_id` 

2. get_order(track_id)
   - Отправляет GET-запрос для получения заказа по переданному `track_id`
   - Возвращает данные заказа в формате JSON

3. def positive_assert_order_creation()
   - Основной тест, который:
     - Вызывает `create__order` для создания нового заказа и получения `track_id`.
     - Проверяет, что код 201 - заказ создан
     - Вызывает `get_order` для получения данных заказа по `track_id`
     - Проверяет, что код 200 - заказ получен

## Запуск тестов

1.  В `configuration.py` указаны значения:
   - `URL_SERVICE` — базовый URL вашего API.
   - `ORDER_CREATE` — путь для создания заказа.
   - `ORDER_NUMBER` — путь для получения заказа по трек-номеру.

2. Запустите файл `test_order.py` для выполнения автотеста
   
Команда для установки зависимостей:

 - pip install -r requirements.txt

Команда для запуска тестов:

 - python test_order.py

Требования

•	Python 3.x
•	Библиотека requests

