import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    drp_userSelect_id = "//select[@id='userSelect']"


    def __init__(self, driver):
        self.driver = driver

    def clickUserDropdown(self):
        wait = WebDriverWait(self.driver, 15)

        dropdown = wait.until(
            EC.presence_of_element_located((By.XPATH, self.drp_userSelect_id))
        )

        wait.until(
            EC.element_to_be_clickable((By.XPATH, self.drp_userSelect_id))
        )
        dropdown.click()

    def selectUser(self, userName):
        element = self.driver.find_element(By.XPATH, f"//option[text()='{userName}']")
        element.click()
