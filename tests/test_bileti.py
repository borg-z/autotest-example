import pytest
import allure
import pytest

# Можем добавить название сайта
@allure.link('https://www.ru')
@allure.step('Ещё один тест')
def test_bileti(driver,baseurl,token):
    driver.get(baseurl)
    # Добавляем в барузер cookie с нашим токеном, чтобы миновать авторизацию
    driver.add_cookie({"name": "session_token", "value": token})
    with allure.step("Показать ещё"):
        driver.find_element_by_css_selector("test").click()
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, attachment_type=allure.attachment_type.PNG)
    driver.find_element_by_css_selector("#test").click()
    with allure.step("Берём первый билет из списка"):
        driver.find_element_by_css_selector(".test img").click()
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, attachment_type=allure.attachment_type.PNG)
    driver.find_element_by_css_selector("#test input").click()
