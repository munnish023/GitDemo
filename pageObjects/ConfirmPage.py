from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    dropdownCountry = (By.LINK_TEXT, "India")


    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)


    def getCountryDrop(self):
        return self.driver.find_element(*ConfirmPage.dropdownCountry)
