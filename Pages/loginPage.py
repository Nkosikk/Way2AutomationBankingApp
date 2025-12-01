from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    btn_custom_login_xpath = "//button[normalize-space(text())='Customer Login']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLogin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.btn_custom_login_xpath)))
        element.click()
