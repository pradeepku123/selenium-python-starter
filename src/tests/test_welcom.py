from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_kickstart():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://localhost:3000/signin')
    driver.maximize_window()

    # Find Element user Name

    web_element_username = driver.find_element_by_id('username')
    web_element_username.clear()
    web_element_username.send_keys('Katharina_Bernier')

    # Find Password

    web_element_password = driver.find_element_by_id('password')
    web_element_password.clear()
    web_element_password.send_keys('s3cret')

    # Click on Submit
    web_element_submit = driver.find_element_by_css_selector(
        '[data-test="signin-submit"]')
    web_element_submit.click()

    time.sleep(7)
    driver.quit()
