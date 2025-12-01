import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/data.ini")


class ReadConfig_data():

    def getURLS(self):
        return config.get("URLS", "dev_url")

    def getCustomerName(self):
        return config.get("login data", "yourName")

