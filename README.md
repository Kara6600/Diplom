# Diplom
# Автоматизация тестирования проекта

## Задача
Автоматизация UI- и API-тестов проекта Кинопоиск из финальной работы по ручному тестированию.

## Структура
- `test/test_ui.py` - UI тесты
- `test/test_api.py` - API тесты
- `configs/` - конфигурационные файлы
- `requirements.txt` - зависимости

## Установка
```bash
pip install -r requirements.txt

Запуск:
Только UI тесты:
bash

pytest -m "ui"

Только API тесты:
bash

pytest -m "api"

Все тесты:
bash

pytest

ссылка на финальный проект по ручному тестированию: https://kartsev-a.yonote.ru/share/68fd1e3f-3cd7-4670-94b2-2ec67e10abe3