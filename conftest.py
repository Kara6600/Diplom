# файлы фикстур pytest (можно для общих настроек)
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Configs.env_config import BASE_URL
from Configs.test_data import cookie_DR

@pytest.fixture
def driver():
    # Создаем вебдрайвер
    driver = webdriver.Chrome()
    # Открываем сайт
    driver.get(BASE_URL)
    # Добавляем cookie
    driver.add_cookie(cookie_DR)
    # Обновляем страницу, чтобы cookie применились
    driver.refresh()

    # Обработка капчи, если есть
    captcha_elements = driver.find_elements(By.CLASS_NAME, 'CheckboxCaptcha-Anchor')
    if captcha_elements:
        captcha_elements[0].click()

    yield driver
    driver.quit()
