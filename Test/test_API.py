import requests
import pytest
import sys
import os
import allure
from Configs.env_config import TOKEN, Url_serch, Accept
from Configs.test_data import (
    Params_SNс,
    Params_SNk,
    Params_SNl,
    Params_SNn,
    Params_SNr
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.api
@allure.feature("API Tests")
@allure.story("Поиск фильма по названию на кирилице")
def test_search_film_by_name_kir():
    with allure.step("Объявление URL и подготовка параметров запроса"):
        url = Url_serch
        params = Params_SNk
        headers = {
            'accept': Accept,
            'X-API-KEY': TOKEN
        }

    with allure.step("Выполнение GET-запроса"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверка статуса ответа"):
        assert (response.status_code == 200), (
            f"Некорректный ответ: {response.status_code}"
        )

    with allure.step("Проверка типа контента ответа"):
        content_type = response.headers.get('Content-Type', '')
        assert content_type.startswith('application/json'), \
            f"Ответ не JSON, Content-Type: {content_type}"

    with allure.step("Парсинг JSON ответа"):
        json_response = response.json()

    with allure.step("Валидация содержимого ответа"):
        assert 'docs' in json_response, "Ключ 'docs' отсутствует в ответе"
        assert isinstance(
            json_response['docs'], list
        ), "'docs' не является списком"
        assert len(json_response['docs']) > 0, "Нет результатов по запросу"

    with allure.step("Вывод названия первого фильма"):
        first_title = json_response['docs'][0].get('title')
        print('Первый фильм в ответе:', first_title)
        # Можно добавить сохранение в отчет
        allure.attach(
            str(first_title) + "\n",  # добавляет перенос строки
            name="Название первого фильма",
            attachment_type=allure.attachment_type.TEXT
        )


@pytest.mark.api
@allure.feature("API Tests")
@allure.story("Поиск фильма по названию на латинице")
def test_search_film_by_name_lat():
    with allure.step("Объявление URL и подготовка параметров запроса"):
        url = Url_serch
        params = Params_SNl
        headers = {
            'accept': Accept,
            'X-API-KEY': TOKEN
        }

    with allure.step("Выполнение GET-запроса"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверка статуса ответа"):
        assert (response.status_code == 200), (
            f"Некорректный ответ: {response.status_code}"
        )

    with allure.step("Проверка типа контента ответа"):
        content_type = response.headers.get('Content-Type', '')
        assert content_type.startswith('application/json'), \
            f"Ответ не JSON, Content-Type: {content_type}"

    with allure.step("Парсинг JSON ответа"):
        json_response = response.json()

    with allure.step("Валидация содержимого ответа"):
        assert 'docs' in json_response, "Ключ 'docs' отсутствует в ответе"
        assert isinstance(
            json_response['docs'], list
            ), "'docs' не является списком"
        assert len(json_response['docs']) > 0, "Нет результатов по запросу"

    with allure.step("Вывод названия первого фильма"):
        first_title = json_response['docs'][0].get('title')
        print('Первый фильм в ответе:', first_title)
        # Можно добавить сохранение в отчет
        allure.attach(
            str(first_title) + "\n",  # добавляет перенос строки
            name="Название первого фильма",
            attachment_type=allure.attachment_type.TEXT
        )


@pytest.mark.api
@allure.feature("API Tests")
@allure.story("Пустой поиск")
def test_search_film_empty():
    with allure.step("Объявление URL и подготовка параметров запроса"):
        url = Url_serch
        params = Params_SNn
        headers = {
            'accept': Accept,
            'X-API-KEY': TOKEN
        }

    with allure.step("Выполнение GET-запроса"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверка статуса ответа"):
        assert (response.status_code == 200), (
            f"Некорректный ответ: {response.status_code}"
        )

    with allure.step("Проверка типа контента ответа"):
        content_type = response.headers.get('Content-Type', '')
        assert content_type.startswith('application/json'), \
            f"Ответ не JSON, Content-Type: {content_type}"

    with allure.step("Парсинг JSON ответа"):
        json_response = response.json()

    with allure.step("Валидация содержимого ответа"):
        assert 'docs' in json_response, "Ключ 'docs' отсутствует в ответе"
        assert isinstance(
            json_response['docs'], list
            ), "'docs' не является списком"
        assert len(json_response['docs']) > 0, "Нет результатов по запросу"

    with allure.step("Вывод названия первого фильма"):
        first_title = json_response['docs'][0].get('title')
        print('Первый фильм в ответе:', first_title)
        # Можно добавить сохранение в отчет
        allure.attach(
            str(first_title) + "\n",  # добавляет перенос строки
            name="Название первого фильма",
            attachment_type=allure.attachment_type.TEXT
        )


@pytest.mark.api
@allure.feature("API Tests")
@allure.story("Поиск фильма по названию с цифрами")
def test_search_film_by_name_num():
    with allure.step("Объявление URL и подготовка параметров запроса"):
        url = Url_serch
        params = Params_SNс
        headers = {
            'accept': Accept,
            'X-API-KEY': TOKEN
        }

    with allure.step("Выполнение GET-запроса"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверка статуса ответа"):
        assert (response.status_code == 200), (
            f"Некорректный ответ: {response.status_code}"
        )

    with allure.step("Проверка типа контента ответа"):
        content_type = response.headers.get('Content-Type', '')
        assert content_type.startswith('application/json'), \
            f"Ответ не JSON, Content-Type: {content_type}"

    with allure.step("Парсинг JSON ответа"):
        json_response = response.json()

    with allure.step("Валидация содержимого ответа"):
        assert 'docs' in json_response, "Ключ 'docs' отсутствует в ответе"
        assert isinstance(
            json_response['docs'], list
            ), "'docs' не является списком"
        assert len(json_response['docs']) > 0, "Нет результатов по запросу"

    with allure.step("Вывод названия первого фильма"):
        first_title = json_response['docs'][0].get('title')
        print('Первый фильм в ответе:', first_title)
        # Можно добавить сохранение в отчет
        allure.attach(
            str(first_title) + "\n",  # добавляет перенос строки
            name="Название первого фильма",
            attachment_type=allure.attachment_type.TEXT
        )


@pytest.mark.api
@allure.feature("API Tests")
@allure.story("Поиск фильма без токена")
def test_search_film_without_token():
    with allure.step("Объявление URL и подготовка параметров запроса"):
        url = Url_serch
        params = Params_SNс
        # Убираем заголовок с токеном, чтобы проверить API без авторизации
        headers = {
            'accept': Accept
        }

    with allure.step("Выполнение GET-запроса"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверка статуса ответа"):
        assert (response.status_code == 401), (
            f"Некорректный ответ: {response.status_code}"
        )

    with allure.step("Проверка типа контента ответа"):
        content_type = response.headers.get('Content-Type', '')
        assert content_type.startswith('application/json'), \
            f"Ответ не JSON, Content-Type: {content_type}"

    with allure.step("Парсинг JSON ответа"):
        json_response = response.json()

    with allure.step("Валидация содержимого ответа"):
        assert 'message' in json_response, "Ключ 'message' отсутствует"
        assert json_response['message'] == "В запросе не указан токен!", \
            f"Неверное сообщение: {json_response.get('message')}"
        assert (
            'error' in json_response and
            json_response['error'] == "Unauthorized"
            ), \
            f"Неверное поле error: {json_response.get('error')}"
        assert (
            'statusCode' in json_response and
            json_response['statusCode'] == 401
            ), \
            f"Неверный статус: {json_response.get('statusCode')}"


@pytest.mark.api
@allure.feature("API Tests")
@allure.story("Поиск с произвольным набором символов")
def test_search_film_by_name_random():
    with allure.step("Объявление URL и подготовка параметров запроса"):
        url = Url_serch
        params = Params_SNr
        headers = {
            'accept': Accept,
            'X-API-KEY': TOKEN
        }

    with allure.step("Выполнение GET-запроса"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверка статуса ответа"):
        assert (response.status_code == 200), (
            f"Некорректный ответ: {response.status_code}"
        )

    with allure.step("Проверка типа контента ответа"):
        content_type = response.headers.get('Content-Type', '')
        assert content_type.startswith('application/json'), \
            f"Ответ не JSON, Content-Type: {content_type}"

    with allure.step("Парсинг JSON ответа"):
        json_response = response.json()

    with allure.step("Валидация содержимого ответа"):
        assert 'docs' in json_response, "Ключ 'docs' отсутствует в ответе"
        assert isinstance(
            json_response['docs'], list
        ), "'docs' не является списком"
        # В случае отсутствия результатов — это допустимо
        # Проверка на пустой список отключена или удалена
        # if len(json_response['docs']) > 0:
        #     first_title = json_response['docs'][0].get('title')
        #     print('Первый фильм в ответе:', first_title)
        # allure.attach(
        #     str(first_title) + "\n",  # добавляет перенос строки
        #     name="Название первого фильма",
        #     attachment_type=allure.attachment_type.TEXT
        # )
    # Версия с выводом первого фильма, если есть результаты
    if json_response['docs']:
        first_title = json_response['docs'][0].get('title')
        print('Первый фильм в ответе:', first_title)
        allure.attach(
            str(first_title) + "\n",  # добавляет перенос строки
            name="Название первого фильма",
            attachment_type=allure.attachment_type.TEXT
        )
    else:
        print('Результатов не найдено.')
        allure.attach(
            "Нет результатов поиска",
            name="Информация",
            attachment_type=allure.attachment_type.TEXT
        )
