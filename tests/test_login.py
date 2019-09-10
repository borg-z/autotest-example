import time
import pytest
import allure

# Название теста в allure
@allure.step('Вход в личный кабинет')
# Передаём параметры полученные в conftest.py
def test_login(driver,username,password,baseurl):
    # Открываем сайт
    driver.get(baseurl)
    # Можем в allure именованные шаги
    with allure.step("Вводидм логин"):
        # Ищем элемент по id  user_login_form_model_phone_number и вводим туда username
        driver.find_element_by_id("user_login_form_model_phone_number").send_keys(username)
        # Получаем скриншот
        attach = driver.get_screenshot_as_png()
        # Прикрепляем скриншот к Allure отчёту
        allure.attach(attach, attachment_type=allure.attachment_type.PNG)
    # Получаем текст элемента по id phone_text
    phone = driver.find_element_by_id("phone_text").text
    # Проверяем соответсвие текста
    assert(phone == username)