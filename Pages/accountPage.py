from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class AccountsPage:

    dropdown_accountsDropdown_id = "//button[normalize-space(text())='Customer Login']"
    dropdown_userSelect_id = "userSelect"
    dropdown_accountSelect_id = "accountSelect"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLogin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_accountsDropdown_id)))
        element.click()

    def select_user_by_text(self, text: str):
        """Select an option from the user dropdown by visible text."""
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.visibility_of_element_located((By.ID, self.dropdown_userSelect_id)))
        Select(dropdown).select_by_visible_text(text)

    def select_account_by_index(self, index: int):
        """Select an account by its value from the account dropdown after login."""
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.element_to_be_clickable((By.ID, self.dropdown_accountSelect_id)))
        Select(dropdown).select_by_index(index)
