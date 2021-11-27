from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from assertpy import assert_that
import time


class Base_Test:
    def setup_browser(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/signin')

    def tear_down(self):
        time.sleep(4)
        self.driver.quit()

    def login_to_application(self):
        self.driver.find_element_by_id(
            'username').send_keys('Katharina_Bernier')
        self.driver.find_element_by_id('password').send_keys('s3cret')
        self.driver.find_element_by_css_selector(
            '[data-test="signin-submit"]').click()

    def find_current_url(self, expected_url):
        assert_that(self.driver.current_url).is_equal_to(expected_url)


def test_navigation():
    driver_boot = Base_Test()
    driver_boot.setup_browser()
    # find Current URL
    driver_boot.find_current_url('http://localhost:3000/signin')
    driver_boot.login_to_application()
    driver_boot.tear_down()
