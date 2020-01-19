import unittest
from selenium import webdriver


class BaseTestClass(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        self.base_url = 'https://sti24-qvalue.xstaging.devfin24.pl/'
        self.registration_url = self.base_url + 'client/register'
        self.driver = webdriver.Chrome(executable_path=r"/Users/aleksandrapalka/drivers/chromedriver")
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.quit()
