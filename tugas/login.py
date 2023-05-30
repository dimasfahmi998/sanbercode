import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):   
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self): #test cases 1
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://myskill.id/")
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]/a[2]").click()
        driver.find_element(By.XPATH, "/html//div[@id='__next']/div[@class='MuiBox-root mui-style-0']/div[@class='mui-style-v82cpl']//form//input[@name='email']").send_keys("dimasfahmi998@gmail.com")
        driver.find_element(By.XPATH, "/html//div[@id='__next']/div[@class='MuiBox-root mui-style-0']/div[@class='mui-style-v82cpl']//form//input[@name='password']").send_keys("dimasfahmi1")
        driver.find_element(By.XPATH, "/html//div[@id='__next']//form/button[@type='submit']").click()

if __name__ == '__main__':
    unittest.main()