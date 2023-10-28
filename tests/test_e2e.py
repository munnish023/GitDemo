import pytest
from selenium.webdriver.common.by import By


from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixture("setup")
class TestOne(BaseClass):

    def test_e2e(self, setup):
        log = self.getLogger()
        log.info("Getting all card titles")

        homePage = HomePage(self.driver)
        homePage.shopItem().click()

        checkOut = CheckoutPage(self.driver)
        phones = checkOut.phonesPage()
    
        for phone in phones:
            phone_title = phone.find_element(By.XPATH, "div/h4/a").text
            log.info(phone_title)
            if phone_title == "Blackberry":
                checkOut.phonePage().click()

        checkOut.getCheckOutBtn().click()

        checkOut.getSuccessBtn().click()

        confirmPage = ConfirmPage(self.driver)
        log.info("Entering country name as Ind")
        confirmPage.getCountry().send_keys("Ind")

        self.verifyLinkPresence("India")

        confirmPage.getCountryDrop().click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()

        msg = self.driver.find_element(By.CLASS_NAME, "alert").text

        log.info("Text received from application is "+ msg)

        assert "Success!" in msg
