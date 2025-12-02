import pytest

from Pages.depositPage import DepositPage
from utils.browserSetUp import setup_Browser
from utils.commonLogin import LoginToWay2AutomationBankingApp
from utils.readProperties_data import ReadConfig_data


class TestWay2AutomationBankingApp:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()
    account1 = ReadConfig_data().getAccount1()
    amountTest1 = ReadConfig_data().getAmountTest1()
    expected_success_message = ReadConfig_data().getDepSuccessMessage()

    @pytest.mark.dev
    def test_loginScenario1(self,setup):
        self.driver = setup_Browser(setup)
        deposit_Page = DepositPage(self.driver)
        expected_success_message = ReadConfig_data().getDepSuccessMessage()


        LoginToWay2AutomationBankingApp(self.driver,self.username,self.account1)

        deposit_Page.clickDepositButton()
        deposit_Page.enterAmount(self.amountTest1)
        deposit_Page.clickSubmitDepositButton()
        success_message = deposit_Page.getDepositSuccessMessage()
        assert success_message == expected_success_message



