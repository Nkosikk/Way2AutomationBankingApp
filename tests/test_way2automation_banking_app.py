import pytest

from utils.browserSetUp import setup_Browser
from utils.commonLogin import LoginToWay2AutomationBankingApp
from utils.readProperties_data import ReadConfig_data


class TestWay2AutomationBankingApp:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()

    @pytest.mark.dev
    def test_login(self,setup):
        self.driver = setup_Browser(setup)

        LoginToWay2AutomationBankingApp(self.driver,self.username)


