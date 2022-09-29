import json
import os

import allure
from appium import webdriver
import pytest
from helpers.log_helper import log_fixture
import applescript

from helpers.utils import get_project_root


@pytest.fixture(scope='session')
def config():
    current_dir = get_project_root()
    conf_path = os.path.join(current_dir, 'config.json')
    with open(conf_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def driver(config):
    log_fixture.info('Starting the WebDriver session')
    desired_capabilities = config["desired_capabilities"]
    remote_url = config["remote_url"]
    driver = webdriver.Remote(command_executor=remote_url,
                              desired_capabilities=desired_capabilities)
    yield driver
    driver.quit()
    log_fixture.info('Stopping the WebDriver session')


@pytest.fixture(autouse=True)
def app(driver, config):
    driver.implicitly_wait(config["wait_time"])
    driver.get(config["application_name"])
    log_fixture.info("Starting the app")
    yield driver
    applescript.tell.app(config["application_name"], "quit")
    log_fixture.info("Closing the app")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    #  get the result of the call to the hook method
    outcome = yield
    rep = outcome.get_result()  # get the test report from the result of the call to the hook method
    # rep.when represents the test step and only gets the use case call  the result of the execution is a failure.
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode):
                if 'driver' in item.fixturenames:
                    web_driver = item.funcargs['driver']
                else:
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),  # add screenshot of allure report
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            log_fixture.info(f'Fail to take screenshot: {e}')
