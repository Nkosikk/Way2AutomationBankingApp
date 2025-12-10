from selenium.webdriver.common.by import By


class TransactionPage:
    btn_transaction_xpath = "//button[contains(text(), 'Transactions')]"
    hdr_transactionDate_xpath = "//table//thead//tr//td[a[contains(text(),'Date-Time')]]"
    lbl_dateTime_xpath = "//table//tbody/tr//td[1]"

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
