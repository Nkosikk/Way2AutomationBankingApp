import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/data.ini")


class ReadConfig_data():

    def getURLS(self):
        return config.get("URLS", "dev_url")

    def getCustomerName(self):
        return config.get("login data", "yourName")

    def getAccountValue(self):
        return config.get("user information", "customerAccount1").strip('"')

    def getDepositAmount(self):
        return config.get("deposit amounts", "amount1")
