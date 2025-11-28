import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    btn_customer_login = "//button[contains(text(), 'Customer Login')]"
    btn_login_xpath= "// button[contains(text(), 'Login')]"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.btn_customer_login)))
        time.sleep(0.5)
        element.click()
        time.sleep(0.10)
        print("Waiting 3 seconds...")
