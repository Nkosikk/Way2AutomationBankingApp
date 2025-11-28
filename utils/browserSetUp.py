from utils.readProperties_data import ReadConfig_data

def setup_Browser(driver):
    dev_url = ReadConfig_data().getURLS()
    driver.get(dev_url)
    driver.maximize_window()
    return driver