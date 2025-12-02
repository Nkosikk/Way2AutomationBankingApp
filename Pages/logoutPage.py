from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LogoutPage:
    btn_logout_id = "//button[contains(text(), 'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        element = self.driver.find_element(By.XPATH, self.btn_logout_id)
        element.click()