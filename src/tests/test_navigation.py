from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_title():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('http://localhost:3000/signin')

    # Return title of String <string 'str'>
    print(type(driver.title))

    time.sleep(6)
    driver.quit()

# Explore Navigation in Selenim


def test_navigation_forward():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('http://localhost:3000/signin')

    # fill the test Data
    driver.find_element_by_id('username').send_keys(tu.test_user['user_name'])
    driver.find_element_by_id('password').send_keys('s3cret')
    driver.find_element_by_css_selector('[data-test="signin-submit"]').click()

    time.sleep(4)
    driver.quit()
    pass
