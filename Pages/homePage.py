import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    btn_customer_login = "//button[contains(text(), 'Customer Login')]"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def clickCustomerLoginButton(self):

        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.btn_customer_login)))
        element.click()


