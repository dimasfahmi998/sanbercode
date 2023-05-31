import unittest
from pageObject.locator import elem
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageObject.data import inputValid
from pageObject.data import inputField


def test_success_login(driver):  # test cases 1 try this one change
    driver.get(inputValid.baseUrl)
    driver.find_element(
        By.ID,
        elem.username,
    ).send_keys(inputValid.username)
    driver.find_element(
        By.ID,
        elem.password,
    ).send_keys(inputValid.Password)
    driver.find_element(By.NAME, elem.loginButton).click()
