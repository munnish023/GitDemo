import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Specify the browser: chrome or Firefox"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()

    request.cls.driver = driver
    request.cls.driver.maximize_window()
    request.cls.driver.get("https://rahulshettyacademy.com/angularpractice/")

    yield

    request.cls.driver.quit()
