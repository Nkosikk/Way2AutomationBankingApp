import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    drp_userSelect_id = "//select[@id='userSelect']"
    btn_login_xpath = "//button[contains(text(), 'Login')]"
    drp_accountSelect_id = "accountSelect"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Instantiate wait globally for class

    def clickUserDropdown(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.drp_userSelect_id))
        )
        dropdown.click()

    def selectUser(self, userName):
        element = self.driver.find_element(By.XPATH, f"//option[text()='{userName}']")
        element.click()

    def clickLoginButton(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.btn_login_xpath))
        )
        element.click()

    def selectAccount(self, accountNumber):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.ID, self.drp_accountSelect_id))
        )
        dropdown.click()
        option = self.driver.find_element(By.XPATH, f"//option[text()='{accountNumber}']")
        option.click()

    def selectAccounts(self, accountNumber):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.ID, self.drp_accountSelect_id))
        )
        select = Select(dropdown)
        select.select_by_visible_text(accountNumber)

