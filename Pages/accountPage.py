from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class AccountsPage:

    dropdown_accountsDropdown_id = "//button[normalize-space(text())='Customer Login']"
    dropdown_userSelect_id = "userSelect"
    dropdown_accountSelect_id = "accountSelect"
    btn_clickDeposit_xpath = "//button[@ng-click='deposit()']"
    enter_amount="//input[@ng-model='amount']"
    btn_clickSubmitDep_xpath ="//button[@type='submit' and normalize-space()='Deposit']"
    lbl_currentBalance_xpath = "//div[@id='account-balance']//strong[@class='ng-binding']"



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

    def click_deposit_Btn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_clickDeposit_xpath)))
        element.click()

    def account_deposit(self, amount1):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.enter_amount)))
        element.send_keys(amount1)

    def clickSubmitDepBtn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_clickSubmitDep_xpath)))
        element.click()

    def getOldBalance(self):
        balance_element = self.driver.find_element(
            By.XPATH, "//div[@ng-hide='noAccount']//strong[@class='ng-binding'][2]"
        )
        balance_text = balance_element.text.strip()
        old_balance = int(balance_text)
        print("Old Balance:", old_balance)
        return old_balance

    def getNewBalance(self,old_balance):
        balance_element = self.driver.find_element(
            By.XPATH, "//div[@ng-hide='noAccount']//strong[@class='ng-binding'][2]"
        )
        balance_text = balance_element.text.strip()
        new_balance = int(balance_text)
        print("New Balance:", new_balance)

        if new_balance > old_balance:
            print("Deposit successful: Balance increased!")
        else:
            print("Deposit may have failed: Balance did not increase.")