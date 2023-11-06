import time
import pytest
from selenium.webdriver.common.by import By
import pytest_check as check
import PageObjects
import BaseApp
from PageObjects import chrome_locators
import allure
from allure_commons.types import AttachmentType




@pytest.mark.usefixtures('setup')
class TestMain:

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("фильтр по цветам")
    def test_section(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть Женщинам"):
            first_question.do_section_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть Обувь"):
            first_question.do_section_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть Фильтр по цветам"):
            first_question.do_section_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Выбрать бежевый цвет"):
            first_question.do_section_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url=="https://www.salita.ru/zhenshchinam/obuv/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("добавить в избранное выбранный товар")
    def test_favorite(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть Одежда"):
            first_question.do_favorite_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Добавить в избранное первый товар"):
            first_question.do_favorite_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть избранное в меню"):
            first_question.do_favorite_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url=="https://www.salita.ru/favorites/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Регистрация пользователя")
    def test_registration(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Заполнить форму регистрации"):
            first_question.do_registration_question("Оксана","+79207776688","dz8ms@yandex.ru","Qwerty.")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Геолокация магазинов")
    def test_shops(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть геолокацию магазинов"):
            first_question.do_shop_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url=="https://www.salita.ru/shops/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Вход пользователя")
    def test_entrance(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Заполнить форму входа"):
            first_question.do_entrance_question("dz8ms@yandex.ru", "Qwerty.")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Тест строки поиска")
    def test_find(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Кликнуть на строку поиска"):
            first_question.do_find_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Ввести в строку поиска запрос"):
            first_question.do_find_question("сапоги\n")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Негативный сценарий теста строки поиска")
    def test_findnegativ(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Кликнуть на строку поиска"):
            first_question.do_findnegativ_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Ввести в строку поиска запрос"):
            first_question.do_findnegativ_question("123456\n")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url=="https://www.salita.ru/?q=123456"


    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Таблица размеров")
    def test_kartopen(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть Одежда"):
            first_question.do_kartopen_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть ссылку на второй товара"):
            first_question.do_kartopen_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть ссылку на Как выбрать"):
            first_question.do_kartopen_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url=="https://www.salita.ru/zhenshchinam/odezhda/dzhempery/658957/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Поиск конкретного товара и его открытие в новом окне")
    def test_newwindow(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Кликнуть на строку поиска"):
            first_question.do_newwindow_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Ввести в строку поиска запрос"):
            first_question.do_newwindow_question("брюки женские BOSS\n")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть ссылку на первый товара"):
            first_question.do_newwindow_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Фильтр сортировки и тест кнопки сбросить")
    def test_filter(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть Одежда"):
            first_question.do_filter_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Кликнуть на сортировку по новинкам"):
            first_question.do_filter_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Выбрать по возрастанию цены"):
            first_question.do_filter_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Кликнуть на Сбросить"):
            first_question.do_filter_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url=="https://www.salita.ru/zhenshchinam/odezhda/filter/clear/apply/"