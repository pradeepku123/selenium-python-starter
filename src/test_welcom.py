from selenium import webdriver
import time
import chromedriver_binary
chromedriver_binary


def test_welcome():
    driver = webdriver.Chrome()
    driver.get('https://demo.testim.io')
    time.sleep(10)
    driver.close()
