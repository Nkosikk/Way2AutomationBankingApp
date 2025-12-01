import pytest

from Pages.loginPage import LoginPage
from utils.readProperties_data import ReadConfig_data

class Test_LoginPage:
    dev_url = ReadConfig_data().getURLS()
    customerName = ReadConfig_data().getCustomerName()

    @pytest.mark.dev
    def test_login_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickCustomerLogin()
        self.lp.selectUserByText(self.customerName)

        self.driver.quit()

        # self.hp = HomePage(self.driver)
        # self.hp.verifyNdosiHeading()
        # self.hp.clickLearningMaterial()
        # self.login = LoginPage(self.driver)
        # self.login.enterEmail(self.username)
        # self.login.enterPassword(self.password)
        # self.login.clickLoginBtn()
