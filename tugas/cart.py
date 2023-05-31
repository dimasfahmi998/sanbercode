import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import base_login
from pageObject.locator import elem
from pageObject.data import inputValid


class TestCart(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):  # test cases 1 try this one change
        driver = self.browser
        driver.get(inputValid.baseUrl)
        base_login.test_success_login(driver)
        driver.find_element(By.ID, elem.addcart).click()
        driver.find_element(By.CLASS_NAME, elem.cart).click()
        currentUrl = driver.current_url
        self.assertIn(currentUrl, inputValid.baseUrl + "/cart.html")


if __name__ == "__main__":
    unittest.main()
