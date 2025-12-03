from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class LoginPage:

    btn_custom_login_xpath = "//button[normalize-space(text())='Customer Login']"
    user_select_id = "userSelect"
    btn_login_xpath = "//button[@class='btn btn-default' and normalize-space(text())='Login']"


    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLogin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.btn_custom_login_xpath)))
        element.click()

    def selectUserByText(self, visible_text):
        """Select an option from the userSelect dropdown by visible text."""
        # local import to avoid duplicate top-level imports if Select isn't already imported

        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.element_to_be_clickable((By.ID, self.user_select_id)))
        select = Select(dropdown)
        select.select_by_visible_text(visible_text)

    def clickLogin(self):

        element = self.driver.find_element(By.XPATH,self.btn_login_xpath)
        element.click()






