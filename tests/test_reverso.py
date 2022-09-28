import allure
import pytest

from app.reverso_page import ReversoPage


class TestTranslationPage:
    @pytest.mark.parametrize("original_word, translation",
                             [("sun", "солнышко "),
                              ("hello", "привет")])
    def test_translate(self, driver, original_word, translation):
        with allure.step("Enter the text into the text field"):
            app_screen = ReversoPage(driver)
            app_screen.search_text(original_word)
        with allure.step("Check that translation is appeared"):
            assert app_screen.translation_label.text == translation, "Translation is not appeared"

    def test_clear_input(self, driver):
        with allure.step("Enter the text into the text field"):
            app_screen = ReversoPage(driver)
            app_screen.search_text("text")
        with allure.step("Clear the text input field"):
            app_screen.clear_input()
        with allure.step("Check that text input is cleared"):
            text_input = app_screen.text_input
            assert text_input.text == "", "Text input is not cleared"

    def test_recent_searches(self, driver):
        with allure.step("Click 'Last searches' button"):
            app_screen = ReversoPage(driver)
            app_screen.open_recent_searches()
        with allure.step("Check that last searches results are appeared"):
            assert app_screen.recent_searches_result_label.text == "hello", "Recent searches results are not appeared"
