import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from urls import URLs


@pytest.fixture(scope="function")
def driver():

    service = Service(GeckoDriverManager().install())
    
    driver = webdriver.Firefox(service=service)
    
    driver.maximize_window()
    
    driver.get(URLs.base_url)
    
    yield driver
    
    driver.quit()