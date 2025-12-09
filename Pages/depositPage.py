from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DepositPage:

    btn_deposit_xpath = "//button[contains(text(), 'Deposit')]"
    txt_amount_xpath = "//input[@placeholder='amount']"
    btn_submitDeposit_xpath = "//button[@type='submit' and contains(text(),'Deposit')]"
    lbl_depositSuccess_xpath = "//div//span[@class='error ng-binding']"
    lbl_balance_xpath = "//div[@class='center']/strong[2]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def clickDepositButton(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_deposit_xpath)))
        element.click()

    def enterAmount(self, amount):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.txt_amount_xpath)))
        element.clear()
        element.send_keys(amount)

    def clickSubmitDepositButton(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_submitDeposit_xpath)))
        element.click()

    def getDepositSuccessMessage(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lbl_depositSuccess_xpath)))
        return element.text

    def getBalance(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lbl_balance_xpath)))
        return int(element.text)






