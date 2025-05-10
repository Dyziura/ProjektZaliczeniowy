import unittest
from selenium import webdriver
from Pages.home_page import HomePage

# z klasy robi się obiekty
class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://petstore.octoperf.com/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
