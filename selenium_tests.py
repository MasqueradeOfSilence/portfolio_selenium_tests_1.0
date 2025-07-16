import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class MyTestCase(unittest.TestCase):

    def test_homepage_title(self):
        driver = webdriver.Chrome(options=webdriver.ChromeOptions())
        driver.get("https://www.alexanderneville.com")
        WebDriverWait(driver, 10).until(ec.title_contains("Alex Neville"))
        print(driver.title)
        assert "Alex Neville" in driver.title
        driver.quit()


if __name__ == '__main__':
    unittest.main()
