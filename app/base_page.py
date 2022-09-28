from typing import Tuple

import allure
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

from helpers.log_helper import log_error, log_operation


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def _get_visible_element(self, locator) -> WebElement:
        try:
            log_operation.info(f'Search element {locator}')
            element = self.wait.until(ec.visibility_of_element_located(locator))
        except NoSuchElementException as e:
            log_error.info(f'Element not found {locator}')
            raise e
        return element

    def _fill_input(self, locator: Tuple[str, str], value: str):
        with allure.step(f"Send text '{value}' to element: {locator}"):
            element = self._get_visible_element(locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click()
            actions.send_keys(value)
            actions.perform()
            log_operation.info(f"Send text '{value}' to element: {locator}")

    def click_on_element(self, locator: Tuple[str, str]):
        print(f"Click on element {locator}")
        with allure.step(f"Click on element {locator}"):
            element = self._get_visible_element(locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click()
            actions.perform()
            log_operation.info(f"Click on element {locator}")
