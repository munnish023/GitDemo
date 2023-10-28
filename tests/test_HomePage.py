import pytest
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.HomePageData import HomePageData


class TestHomePage(BaseClass):

    @pytest.mark.usefixtures("setup")
    def test_forSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPwd().send_keys("1234")
        homepage.getCheckBox().click()

        self.select_by_visble_text(homepage.getDropdown(),getData["gender"])


        homepage.getRadioBtn().click()
        homepage.getSubmit().click()

        alert = homepage.getAlert().text

        assert "Success" in alert
        print(getData["firstname"],getData["lastname"],getData["gender"])
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param


print("This is a print")
