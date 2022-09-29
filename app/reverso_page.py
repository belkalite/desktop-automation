from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from app.base_page import BasePage


class ReversoPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.text_input_locator = (By.XPATH,
                                   "/AXApplication[@AXTitle='Reverso']/AXWindow[@AXTitle='Reverso' and @AXIdentifier='_NS:14' and @AXSubrole='AXStandardWindow']/AXGroup[@AXIdentifier='_NS:38']/AXGroup[0]/AXScrollArea[0]/AXWebArea[0]/AXTextArea[@AXDOMIdentifier='wordInput']")
        self.search_button_locator = (By.XPATH,
                                      "/AXApplication[@AXTitle='Reverso']/AXWindow[@AXTitle='Reverso' and @AXIdentifier='_NS:14' and @AXSubrole='AXStandardWindow']/AXGroup[@AXIdentifier='_NS:38']/AXGroup[0]/AXScrollArea[0]/AXWebArea[0]/AXButton[4]")

        self.translation_locator = (By.XPATH,
                                    "/AXApplication[@AXTitle='Reverso']/AXWindow[@AXTitle='Reverso' and @AXIdentifier='_NS:14' and @AXSubrole='AXStandardWindow']/AXGroup[@AXIdentifier='_NS:38']/AXGroup[0]/AXScrollArea[0]/AXWebArea[0]/AXGroup[7]/AXStaticText"
                                    )
        self.clear_input_locator = (By.XPATH,
                                    "/AXApplication[@AXTitle='Reverso']/AXWindow[@AXTitle='Reverso' and @AXIdentifier='_NS:14' and @AXSubrole='AXStandardWindow']/AXGroup[@AXIdentifier='_NS:38']/AXGroup[0]/AXScrollArea[0]/AXWebArea[0]/AXButton[4]")
        self.recent_searches_locator = (By.XPATH,
                                        "/AXApplication[@AXTitle='Reverso']/AXWindow[@AXTitle='Reverso' and @AXIdentifier='_NS:14' and @AXSubrole='AXStandardWindow']/AXGroup[@AXIdentifier='_NS:38']/AXGroup[0]/AXScrollArea[0]/AXWebArea[0]/AXGroup[@AXSubrole='AXContentList']/AXHeading[@AXTitle='RECENT SEARCHES']/AXGroup[0]/AXStaticText[@AXValue='RECENT SEARCHES']"
                                        )
        self.recent_searches_result_locator = (By.XPATH,
                                               "/AXApplication[@AXTitle='Reverso']/AXWindow[@AXTitle='Reverso' and @AXIdentifier='_NS:14' and @AXSubrole='AXStandardWindow']/AXGroup[@AXIdentifier='_NS:38']/AXGroup[0]/AXScrollArea[0]/AXWebArea[0]/AXGroup[@AXSubrole='AXContentList']/AXGroup[0]/AXGroup[0]/AXStaticText")

    @property
    def text_input(self):
        return self._get_visible_element(self.text_input_locator)

    @property
    def search_button(self):
        return self.driver.find_element(*self.search_button_locator)

    def click_search(self):
        self._get_visible_element(self.search_button_locator).click()

    @property
    def translation_label(self):
        return self._get_visible_element(self.translation_locator)

    def search_text(self, value: str):
        self.enter_text(value)
        self.click_on_element(self.search_button_locator)

    def enter_text(self, value: str):
        self._fill_input(self.text_input_locator, value)

    def clear_input(self):
        self.click_on_element(self.clear_input_locator)

    def open_recent_searches(self):
        self.click_on_element(self.recent_searches_locator)

    @property
    def recent_searches_result_label(self):
        return self._get_visible_element(self.recent_searches_result_locator)
