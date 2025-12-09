import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/data.ini")


class ReadConfig_data():

    def getURLS(self):
        return config.get("URLS", "dev_url")

    def getUsername(self):
        return config.get("login data", "username")

    def getAccount1(self):
        return config.get("Test Data", "account1")

    def getAmountTest1(self):
        return config.get("Test Data", "amountTest1")

    def getAccount2(self):
        return config.get("Test Data", "account2")

    def getAmountTest2(self):
        return config.get("Test Data", "amountTest2")

    def getAccount3(self):
        return config.get("Test Data", "account3")

    def getAmountTest3(self):
        return config.get("Test Data", "amountTest3")

    def getDepSuccessMessage(self):
        return config.get("Test Data", "successMessage")
