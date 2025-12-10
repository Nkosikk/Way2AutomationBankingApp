
import time

import pytest

from Pages.depositPage import DepositPage
from Pages.loginPage import LoginPage
from Pages.logoutPage import LogoutPage
from Pages.transactionPage import TransactionPage
from utils.browserSetUp import setup_Browser
from utils.commonLogin import LoginToWay2AutomationBankingApp
from utils.readProperties_data import ReadConfig_data
from datetime import datetime


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

    @pytest.mark.dev
    def test_scenario3(self, setup):
        self.driver = setup_Browser(setup)

        login_Page = LoginPage(self.driver)
        deposit_Page = DepositPage(self.driver)
        transactions_Page = TransactionPage(self.driver)
        logout_Page = LogoutPage(self.driver)
        expected_success_message = ReadConfig_data().getDepSuccessMessage()

        LoginToWay2AutomationBankingApp(self.driver, self.username)
        login_Page.selectAccount(int(self.account3))

        # Capture initial balance
        initial_balance = deposit_Page.getBalance()
        print("This is the initial balance: ", initial_balance)

        # Make a deposit
        deposit_Page.clickDepositButton()
        deposit_Page.enterAmount(int(self.amountTest3))
        deposit_Page.clickSubmitDepositButton()
        time.sleep(2)

        transaction_time = datetime.now().strftime("%b %d, %Y %I:%M:%S %p")
        print("Recorded transaction time:", transaction_time)

        fmt = "%b %d, %Y %I:%M:%S %p"  # Matching UI format

        # Record transaction time
        expected_dt = datetime.strptime(transaction_time, fmt)
        print("Expected transaction datetime: ", expected_dt)

        # Verify success message and updated balance
        success_message = deposit_Page.getDepositSuccessMessage()
        assert success_message == expected_success_message

        # Verify balance update
        new_balance = deposit_Page.getBalance()
        assert int(new_balance) == int(initial_balance) + int(self.amountTest3), \
            f"Expected balance: {initial_balance + self.amountTest3}, Actual: {new_balance}"
        print("This is a new balance: ", new_balance)

        transactions_Page.clickTransactionButton()
        time.sleep(2)
        transactions_Page.clickTransactionDateHeader()
        time.sleep(2)


        latest_dt = transactions_Page.getTransactionDateTime()
        time.sleep(2)
        print("Transaction datetime from UI:", latest_dt)
        actual_dt = datetime.strptime(latest_dt, fmt)

        time_diff = abs((expected_dt - actual_dt).total_seconds())

        assert time_diff <= 5, \
            f"Time drift too large! Expected {transaction_time}, Got {latest_dt}. Diff: {time_diff} sec"

        print("Transaction datetime verified:", actual_dt)

        # Verify transaction amount
        transaction_amount = transactions_Page.getTransactionAmount()
        assert transaction_amount == str(self.amountTest3), \
            f"Amount mismatch! Expected: {self.amountTest3}, Got: {transaction_amount}"
        print("Transaction amount verified:", transaction_amount)


        #Withdraw money
        transactions_Page.clickBackButton()
        time.sleep(1)
        transactions_Page.clickWithdrawButton()
        time.sleep(1)
        deposit_Page.enterAmount(int(self.amountTest3))
        transactions_Page.clickPerformWithdrawButton()
        time.sleep(2)

        # Verify withdrawal success message
        withdrawl_success_message = transactions_Page.getWithdrawSuccessMessage()
        expected_success_message = ReadConfig_data().getWithdrawSuccessMessage()
        assert withdrawl_success_message == expected_success_message
        print("Withdrawl success message verified:", withdrawl_success_message)

        # Verify remaining balance after withdrawal
        after_withdrawal_balance = deposit_Page.getBalance()
        print("This is the balance after withdrawal: ",  after_withdrawal_balance)

        expected_remaining_balance = new_balance - int(self.amountTest3)

        assert int(after_withdrawal_balance) == expected_remaining_balance, \
            f"Expected remaining balance: {expected_remaining_balance}, Actual: {after_withdrawal_balance}"
        print("Remaining balance after withdrawal verified:", after_withdrawal_balance)

#     View transaction history to confirm withdrawal
        transactions_Page.clickTransactionButton()
        time.sleep(1)

        fmt = "%b %d, %Y %I:%M:%S %p"  # Example: Dec 10, 2025 04:19:07 PM

        #Capture EXPECTED timestamp immediately after clicking
        withdrawal_time = datetime.now().strftime(fmt)
        expected_dt_withdrawal = datetime.strptime(withdrawal_time, fmt)
        print("Expected withdrawal timestamp:", withdrawal_time)

        #Sort the table by Date-Time (DESC)
        transactions_Page.clickTransactionDateHeader()
        time.sleep(1)

        #Get the latest transaction DateTime from UI
        latest_dt_text = transactions_Page.getTransactionDateTime()
        print("Latest withdrawal Date-Time from UI:", latest_dt_text)

        #Convert UI timestamp → datetime object
        actual_dt_withdraw = datetime.strptime(latest_dt_text, fmt)

        #Compare timestamps with tolerance
        time_diff_seconds = abs((expected_dt_withdrawal - actual_dt_withdraw).total_seconds())
        print("Timestamp difference (sec):", time_diff_seconds)

        assert time_diff_seconds <= 5, (
            f"Withdrawal timestamp mismatch!\n"
            f"Expected: {withdrawal_time}\n"
            f"Got:      {latest_dt_text}\n"
            f"Diff:     {time_diff_seconds} seconds"
        )

        print("Withdrawal timestamp verified successfully:", actual_dt_withdraw)

        # Verify withdrawal transaction amount
        transaction_amount_withdraw = transactions_Page.getTransactionAmount()
        expected_withdraw_amount = int(self.amountTest3)
        assert transaction_amount_withdraw == str(expected_withdraw_amount), \
            f"Withdrawal amount mismatch! Expected: {expected_withdraw_amount}, Got: {transaction_amount_withdraw}"
        print("Withdrawal transaction amount verified:", transaction_amount_withdraw)

        logout_Page.clickLogoutButton()
