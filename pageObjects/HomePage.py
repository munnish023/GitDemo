from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radioBtn = (By.CSS_SELECTOR, "input[id='inlineRadio1']")
    submit = (By.XPATH, "(//input[@value='Submit'])")
    binding = (By.XPATH, "(//input[@name='name'])[2]")
    alert = (By.CLASS_NAME, "alert")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPwd(self):
        return self.driver.find_element( *HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element( *HomePage.checkBox)

    def getDropdown(self):
        return self.driver.find_element( *HomePage.dropdown)

    def getRadioBtn(self):
        return self.driver.find_element( *HomePage.radioBtn)

    def getSubmit(self):
        return self.driver.find_element( *HomePage.submit)

    def getBinding(self):
        return self.driver.find_element( *HomePage.binding)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)
