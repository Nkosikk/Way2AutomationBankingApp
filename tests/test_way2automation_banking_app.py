import pytest

from Pages.depositPage import DepositPage
from Pages.loginPage import LoginPage
from Pages.logoutPage import LogoutPage
from utils.browserSetUp import setup_Browser
from utils.commonLogin import LoginToWay2AutomationBankingApp
from utils.readProperties_data import ReadConfig_data


class TestWay2AutomationBankingApp:
    dev_url = ReadConfig_data().getURLS()

    username = ReadConfig_data().getUsername()
    account1 = ReadConfig_data().getAccount1()
    account2 = ReadConfig_data().getAccount2()
    account3 = ReadConfig_data().getAccount3()

    amountTest1 = ReadConfig_data().getAmountTest1()
    amountTest2 = ReadConfig_data().getAmountTest2()
    amountTest3 = ReadConfig_data().getAmountTest3()

    expected_success_message = ReadConfig_data().getDepSuccessMessage()

    @pytest.mark.dev
    def test_Scenario1(self,setup):
        self.driver = setup_Browser(setup)

        login_Page = LoginPage(self.driver)
        deposit_Page = DepositPage(self.driver)
        logout_Page = LogoutPage(self.driver)
        expected_success_message = ReadConfig_data().getDepSuccessMessage()


        LoginToWay2AutomationBankingApp(self.driver,self.username)
        login_Page.selectAccount(int(self.account1))

        # Capture initial balance
        initial_balance = deposit_Page.getBalance()
        print("This is the initial balance: ",initial_balance)

        # Make a deposit
        deposit_Page.clickDepositButton()
        deposit_Page.enterAmount(int(self.amountTest1))
        deposit_Page.clickSubmitDepositButton()

        # Verify success message and updated balance
        success_message = deposit_Page.getDepositSuccessMessage()
        assert success_message == expected_success_message

        # Verify balance update
        new_balance = deposit_Page.getBalance()
        assert int(new_balance) == int(initial_balance)+ int(self.amountTest1), \
        f"Expected balance: {initial_balance + self.amountTest1}, Actual: {new_balance}"
        print("This is a new balance: ",new_balance)
        logout_Page.clickLogoutButton()

    @pytest.mark.dev
    @pytest.mark.parametrize("accountNumber", [account1, account2, account3])
    def test_deposit_per_account(self, setup, accountNumber):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()

        login_Page = LoginPage(self.driver)
        deposit_Page = DepositPage(self.driver)
        logout_Page = LogoutPage(self.driver)
        expected_success_message = ReadConfig_data().getDepSuccessMessage()

        # Login
        LoginToWay2AutomationBankingApp(self.driver, self.username)

        # Select each account
        login_Page.selectAccounts(accountNumber)
        print(f"\nSelected Account: {accountNumber}")

        # Initial balance
        initial_balance = int(deposit_Page.getBalance())
        print("Initial Balance:", initial_balance)

        # Deposit
        deposit_Page.clickDepositButton()
        deposit_Page.enterAmount(self.amountTest2)
        deposit_Page.clickSubmitDepositButton()

        # Validate receipt message
        success_msg = deposit_Page.getDepositSuccessMessage()
        assert success_msg == expected_success_message

        # Verify balance update
        new_balance = int(deposit_Page.getBalance())
        expected_balance = int(initial_balance) + int(self.amountTest2)

        assert new_balance == expected_balance, \
            f"Balance mismatch! Expected: {expected_balance}, Got: {new_balance} | Initial: {initial_balance} + Deposit: {self.amountTest2}"

        print(f"New Balance Verified for Account {accountNumber}: {new_balance}")

        # Logout
        logout_Page.clickLogoutButton()


