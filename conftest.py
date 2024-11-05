import pytest
import requests
from selenium import webdriver
from helpers import CreateUser
from locators.repair_password import RepairPasswordLocators
from data import Urls
from pages.order_feed_page import OrderFeed
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.lk_page import PersonalAccountPage
from pages.repair_password_page import RepairPassword
import data


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        data.driver_name = 'chrome'
        driver.set_window_size(1920, 1080)
        driver.get(Urls.URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        data.driver_name = 'firefox'
        driver.set_window_size(1920, 1080)
        driver.get(Urls.URL)
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def header_page(driver):
    return HeaderPage(driver)


@pytest.fixture()
def order_page(driver):
    return OrderFeed(driver)


@pytest.fixture()
def lk_page(driver):
    return PersonalAccountPage(driver)


@pytest.fixture()
def repair_page(driver):
    return RepairPassword(driver)


@pytest.fixture()
def create_new_user():
    login_password = CreateUser.register_new_user_and_return_login_password()
    data = {"name": login_password[0], "email": login_password[1], "password": login_password[2]}
    response = requests.post(Urls.URL + Urls.CREATE_USER, data=data)
    access_token = response.json().get('accessToken')
    yield login_password
    requests.delete(Urls.URL + Urls.ACTION_USER, headers={'authorization': f'{access_token}'})


@pytest.fixture()
def authorization_user(driver, create_new_user):
    main_page = HeaderPage(driver)
    main_page.click_lk_page()
    login_page = RepairPassword(driver)
    login_page.add_text_to_element(RepairPasswordLocators.INPUT_EMAIL, create_new_user[1])
    login_page.add_text_to_element(RepairPasswordLocators.INPUT_PASSWORD, create_new_user[2])
    login_page.click_element_with_wait(RepairPasswordLocators.ENTER_BUTTON)



