from Pages.homePage import HomePage
from Pages.loginPage import LoginPage

def LoginToWay2AutomationBankingApp(driver,username):
    hp = HomePage(driver)
    hp.clickCustomerLoginButton()
    login=LoginPage(driver)
    login.clickUserDropdown()
    login.selectUser(username)



