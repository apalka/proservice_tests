from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

default_timeout = 10


def wait_for_element(driver, xpath, timeout=default_timeout):
    element_present = ec.visibility_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, timeout).until(element_present)


def wait_for_elements(driver, xpath, timeout=default_timeout):
    elements_present = ec.visibility_of_any_elements_located((By.XPATH, xpath))
    WebDriverWait(driver, timeout).until(elements_present)








