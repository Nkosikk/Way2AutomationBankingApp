import time

import pytest

from Pages.loginPage import LoginPage
from Pages.accountPage import AccountsPage
from utils.readProperties_data import ReadConfig_data

class Test_LoginPage:
    dev_url = ReadConfig_data().getURLS()
    customerName = ReadConfig_data().getCustomerName()
    amount1= ReadConfig_data().getDepositAmount()


    @pytest.mark.dev
    def test_login_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickCustomerLogin()
        self.lp.selectUserByText(self.customerName)
        self.lp.clickLogin()
        self.ap = AccountsPage(self.driver)
        self.ap.select_account_by_index(0)
        self.ap.click_deposit_Btn()
        self.ap.account_deposit(self.amount1)
        self.ap.clickSubmitDepBtn()
        time.sleep(10)
        self.driver.quit()
