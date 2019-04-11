from selenium import webdriver
import pytest
from pages.loginpage import LoginPage

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    # @pytest.fixture(scope='session')
    # def test_setup(self):
    #      global driver
    #      driver=webdriver.Chrome()
    #      driver.get("http://localhost:8080/login?from=%2F")
    #      driver.maximize_window()
    #      driver.implicitly_wait(30)
    #      yield
    #      driver.quit()

    def test_login(self, test_setup):
        driver=self.driver
        lp = LoginPage(driver)
        lp.enter_un()
        lp.enter_pwd()
        lp.click_on_login_btn()

        # driver.find_element_by_name("j_username").send_keys("admin")
        # driver.find_element_by_name("j_password").send_keys("dcf4d75933c5462abded5ea412fe236b")
        # driver.find_element_by_name("Submit").click()

    def test_logout(self, test_setup):
        driver = self.driver
        driver.find_element_by_xpath("//*[text()='log out']").click()



