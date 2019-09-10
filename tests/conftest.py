import pytest
from pytest import fixture
from selenium import webdriver
import allure
import logging
import os


@pytest.fixture(scope='module')
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(15)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    def fin():
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, attachment_type=allure.attachment_type.PNG)
        logging.info("Closing webdriver instance")
        driver.quit()
    yield driver
    request.addfinalizer(fin)



@pytest.fixture(scope='session')
def baseurl(request):
    baseurl = os.environ.get('BASEURL')
    return baseurl

@pytest.fixture(scope='session')
def username(request):
    username = os.environ.get('USERNAME')
    return username

@pytest.fixture(scope='session')
def password(request):
    password = os.environ.get('PASSWORD')
    return password

@pytest.fixture(scope='session')
def token(request):
    token = os.environ.get('TOKEN')
    return token