from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    phones = (By.XPATH, "//div[@class='card h-100']")
    phone_button = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkOutBtn = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    successBtn = (By.CSS_SELECTOR, ".btn.btn-success")

    def phonesPage(self):
        return self.driver.find_elements(*CheckoutPage.phones)

    def phonePage(self):
        return self.driver.find_element(*CheckoutPage.phone_button)

    def getCheckOutBtn(self):
        return self.driver.find_element(*CheckoutPage.checkOutBtn)

    def getSuccessBtn(self):
        return self.driver.find_element(*CheckoutPage.successBtn)
