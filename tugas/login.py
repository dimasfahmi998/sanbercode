import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):  # test cases 1 try this one change
        baseUrl = "https://myskill.id/"
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        driver.find_element(
            By.XPATH,
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]/a[2]",
        ).click()
        driver.find_element(
            By.XPATH,
            "/html//div[@id='__next']/div[@class='MuiBox-root mui-style-0']/div[@class='mui-style-v82cpl']//form//input[@name='email']",
        ).send_keys("dimasfahmi998@gmail.com")
        driver.find_element(
            By.XPATH,
            "/html//div[@id='__next']/div[@class='MuiBox-root mui-style-0']/div[@class='mui-style-v82cpl']//form//input[@name='password']",
        ).send_keys("dimasfahmi1")
        driver.find_element(
            By.XPATH, "/html//div[@id='__next']//form/button[@type='submit']"
        ).click()

    def test_success_orange_login(self):  # test case 2
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']",
        ).click()

    def test_field_orange_login(self):  # test case 3
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']",
        ).click()


if __name__ == "__main__":
    unittest.main()
