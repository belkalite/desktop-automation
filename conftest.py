from appium import webdriver
import pytest
from helpers.log_helper import log_fixture
import applescript


@pytest.fixture(scope='session')
def driver():
    log_fixture.info('Starting the WebDriver session')
    desired_capabilities = {
        "platformName": "Mac",
        "deviceName": "mac",
        "platformVersion": "12.4",
        "automationName": "mac2",
        # "bundleId": "com.softissimo.ReversoContext.macosapp"
    }
    driver = webdriver.Remote(command_executor='http://localhost:4622/wd/hub',
                              desired_capabilities=desired_capabilities)
    yield driver
    driver.quit()
    log_fixture.info('Stopping the WebDriver session')


@pytest.fixture(autouse=True)
def app(driver):
    driver.get("Reverso")
    log_fixture.info('Starting the app')
    yield driver
    applescript.tell.app("Reverso", "quit")
    log_fixture.info('Closing the app')
