# UI тесты
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import sys
import os
from Configs.env_config import BASE_URL
from Configs.test_data import cookie_DR
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


service = ChromeService(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


@pytest.fixture
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.ui
@allure.feature("UI Tests")
@allure.title("поиск по названию")
def test_kinopoisk_search(driver):
    try:
        with allure.step("Переход на страницу 'https://www.kinopoisk.ru'"):
            driver.get(BASE_URL)

        with allure.step("Добавляем куки и обновляем страницу"):
            driver.add_cookie(cookie_DR)
            driver.refresh()

        wait = WebDriverWait(driver, 10)

        with allure.step("Ждем чекбокс 'CheckboxCaptcha-Anchor' и кликаем"):
            checkbox_anchor = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'CheckboxCaptcha-Anchor')
                )
            )
            checkbox_anchor.click()

        with allure.step("Ждем поле поиска 'kp_query' и вводим запрос 'Оно'"):
            input_field = wait.until(
                EC.presence_of_element_located(
                    (By.NAME, "kp_query")
                )
            )
            input_field.clear()
            input_field.send_keys("Оно")
            input_field.send_keys(Keys.ENTER)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


@pytest.mark.ui
@allure.feature("UI Tests")
@allure.title("Выставление оценки фильму на Кинопоиске")
def test_kinopoisk_review(driver):
    try:
        with allure.step("Переход на страницу 'https://www.kinopoisk.ru'"):
            driver.get(BASE_URL)

        with allure.step("Добавляем куки и обновляем страницу"):
            driver.add_cookie(cookie_DR)
            driver.refresh()

        wait = WebDriverWait(driver, 10)

        with allure.step("Ждем чекбокс 'CheckboxCaptcha-Anchor' и кликаем"):
            checkbox_anchor = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'CheckboxCaptcha-Anchor')
                    )
                )
            checkbox_anchor.click()

        with allure.step("Ждем поле поиска 'kp_query' и вводим запрос 'Оно'"):
            input_field = wait.until(
                EC.presence_of_element_located(
                    (By.NAME, "kp_query")
                    )
                )
            input_field.clear()
            input_field.send_keys("Оно")
            input_field.send_keys(Keys.ENTER)

        with allure.step("ищем карточку фильма 'Оно' и кликаем на нее"):
            element = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//a[@class='js-serp-metrika' and"
                " normalize-space(text())='Оно']"
            )))
            element.click()

        with allure.step("Кликаем кнопку 'Оценить фильм'"):
            button = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                'button.style_button__Awsrq.style_buttonSize32__0wbvn.'
                'style_buttonPrimary__Qn_9l.style_buttonLight__C8cK7.'
                'style_fullWidth__EUzsK'
            )))
            button.click()

        with allure.step("Выбираем оценку '7'"):
            rating_element = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[@class='styles_itemValue__8hM9K' and text()='7']"
            )))
            rating_element.click()
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Оценка_фильма",
                attachment_type=allure.attachment_type.PNG
            )

    except Exception:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Ошибка",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    finally:
        driver.quit()


@pytest.mark.ui
@allure.feature("UI Tests")
@allure.title("Поиск по жанру на Кинопоиске")
def test_kinopoisk_search_genre(driver):
    try:
        with allure.step("Открываем страницу 'https://www.kinopoisk.ru'"):
            driver.get(BASE_URL)

        with allure.step("Добавляем куки и обновляем страницу"):
            driver.add_cookie(cookie_DR)
            driver.refresh()

        wait = WebDriverWait(driver, 10)

        with allure.step("Ждем и кликаем чекбокс 'CheckboxCaptcha-Anchor'"):
            wait = WebDriverWait(driver, 10)
            checkbox_anchor = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'CheckboxCaptcha-Anchor')
                )
            )
            checkbox_anchor.click()
        with allure.step("Кликаем на расширенный поиск (иконка SVG)"):
            svg_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR,
                    "svg.styles_advancedSearchIconActive__EwWRU."
                    "styles_advancedSearchIcon__u9ckM"
                ))
            )
            svg_element.click()

        with allure.step("Выбираем жанр 'боевик' (value='3')"):
            select_element = wait.until(
                EC.presence_of_element_located(
                    (By.ID, "m_act[genre]")
                    )
                )
            select = Select(select_element)
            select.select_by_value("3")

        with allure.step("Прокручиваем страницу вниз"):
            driver.execute_script("window.scrollBy(0, 100);")

        with allure.step("Кликаем по чекбоксу 'm_act[genre_and]'"):
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "m_act[genre_and]"))
            )
            checkbox.click()

        with allure.step("Кликаем по кнопке поиска"):
            button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        'input.el_18.submit.nice_button[type="button"]'
                    )
                )
            )
            button.click()

    finally:
        driver.quit()


@pytest.mark.ui
@allure.feature("UI Tests")
@allure.title("поиск по стране")
def test_kinopoisk_search_coutry(driver):
    try:
        with allure.step("Открываем страницу 'https://www.kinopoisk.ru'"):
            driver.get(BASE_URL)

        with allure.step("Добавляем куки и обновляем страницу"):
            driver.add_cookie(cookie_DR)
            driver.refresh()

        with allure.step("Ждем и кликаем чекбокс 'CheckboxCaptcha-Anchor'"):
            wait = WebDriverWait(driver, 10)
            checkbox_anchor = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'CheckboxCaptcha-Anchor')
                )
            )
            checkbox_anchor.click()

        with allure.step("Кликаем на расширенный поиск (иконка SVG)"):
            svg_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR,
                    "svg.styles_advancedSearchIconActive__EwWRU."
                    "styles_advancedSearchIcon__u9ckM"
                ))
            )
            svg_element.click()

        with allure.step("Выбираем страну 'Россия' (value='2') в селекторе"):
            wait = WebDriverWait(driver, 10)
            select_element = wait.until(
                EC.presence_of_element_located(
                    (By.ID, "country")
                    )
                )
            select = Select(select_element)
            select.select_by_value("2")

        with allure.step("Выбираем жанр 'боевик' (value='3')"):
            select_element = wait.until(
                EC.presence_of_element_located(
                    (By.ID, "m_act[genre]")
                    )
                )
            select = Select(select_element)
            select.select_by_value("3")

        with allure.step("Прокручиваем страницу вниз"):
            driver.execute_script("window.scrollBy(0, 600);")

        with allure.step("Кликаем по чекбоксу 'm_act[genre_and]'"):
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "m_act[genre_and]"))
            )
            checkbox.click()

        with allure.step("Кликаем по кнопке поиска"):
            button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        'input.el_18.submit.nice_button[type="button"]'
                    )
                )
            )
            button.click()

    finally:
        driver.quit()


@pytest.mark.ui
@allure.feature("UI Tests")
@allure.title("# поиск сериалов в период времени")
def test_kinopoisk_search_time_dist(driver):
    try:
        with allure.step("Открываем страницу 'https://www.kinopoisk.ru'"):
            driver.get(BASE_URL)

        with allure.step("Добавляем куки и обновляем страницу"):
            driver.add_cookie(cookie_DR)
            driver.refresh()

        with allure.step("Ждем и кликаем чекбокс 'CheckboxCaptcha-Anchor'"):
            wait = WebDriverWait(driver, 10)
            checkbox_anchor = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'CheckboxCaptcha-Anchor')
                )
            )
            checkbox_anchor.click()

        with allure.step("Кликаем на расширенный поиск SVG"):
            svg_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR,
                    "svg.styles_advancedSearchIconActive__EwWRU."
                    "styles_advancedSearchIcon__u9ckM"
                ))
            )
            svg_element.click()

        with allure.step("Выбираем диапазон годов 2010 - 2020"):
            wait = WebDriverWait(driver, 10)

            # От 2010
            select_from_year = wait.until(
                EC.presence_of_element_located(
                    (By.ID, "from_year")
                    )
                )
            select_from = Select(select_from_year)
            select_from.select_by_value("2010")

            # До 2020
            select_to_year = wait.until(
                EC.presence_of_element_located(
                    (By.ID, "to_year")
                    )
                )
            select_to = Select(select_to_year)
            select_to.select_by_value("2020")

        with allure.step("Выбираем страну 'Россия' (value='2')"):
            select_country = wait.until(
                EC.presence_of_element_located(
                    (By.ID, "country")
                    )
                )
            select = Select(select_country)
            select.select_by_value("2")

        with allure.step("Выбираем жанр 'боевик'"):
            select_genre = wait.until(
                EC.presence_of_element_located(
                    (By.ID, "m_act[genre]")
                    )
                )
            select = Select(select_genre)
            select.select_by_value("3")

        with allure.step("Прокрутка вниз и выбор 'Serial' в сериалите"):
            driver.execute_script("window.scrollBy(0, 600);")
            select_serials = driver.find_element(
                By.CSS_SELECTOR, 'select.text.el_17'
            )
            select = Select(select_serials)
            select.select_by_value("serial")

        with allure.step("Кликаем по чекбоксу 'm_act[genre_and]'"):
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "m_act[genre_and]"))
            )
            checkbox.click()

        with allure.step("Кликаем по кнопке поиска"):
            button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        'input.el_18.submit.nice_button[type="button"]'
                    )
                )
            )
            button.click()

    finally:
        driver.quit()
