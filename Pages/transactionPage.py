from selenium.webdriver.common.by import By


class TransactionPage:
    btn_transaction_xpath = "//button[contains(text(), 'Transactions')]"
    hdr_transactionDate_xpath = "//table//thead//tr//td[a[contains(text(),'Date-Time')]]"
    lbl_dateTime_xpath = "//table//tbody/tr//td[1]"
    lbl_amount_xpath = "//table//tbody/tr//td[2]"
    btn_back_xpath = "//button[contains(text(), 'Back')]"
    btn_withdraw_xpath = "//button[contains(text(), 'Withdrawl')]"
    btn_performWithdraw_xpath = "//button[text()='Withdraw']"
    lbl_withdrawlSuccess_xpath = "//div//span[@class='error ng-binding']"

    def __init__(self, driver):
        self.driver = driver

    def clickTransactionButton(self):
        element = self.driver.find_element(By.XPATH, self.btn_transaction_xpath)
        element.click()

    def clickTransactionDateHeader(self):
        element = self.driver.find_element(By.XPATH, self.hdr_transactionDate_xpath)
        element.click()

    def getTransactionDateTime(self):
        element = self.driver.find_element(By.XPATH, self.lbl_dateTime_xpath)
        return element.text

    def getTransactionAmount(self):
        element = self.driver.find_element(By.XPATH, self.lbl_amount_xpath)
        return element.text

    def clickBackButton(self):
        element = self.driver.find_element(By.XPATH, self.btn_back_xpath)
        element.click()

    def clickWithdrawButton(self):
        element = self.driver.find_element(By.XPATH, self.btn_withdraw_xpath)
        element.click()

    def clickPerformWithdrawButton(self):
        element = self.driver.find_element(By.XPATH, self.btn_performWithdraw_xpath)
        element.click()

    def getWithdrawSuccessMessage(self):
        element = self.driver.find_element(By.XPATH, self.lbl_withdrawlSuccess_xpath)
        return element.text