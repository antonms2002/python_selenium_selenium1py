import allure

from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    SUCCESS_MESSAGE_TEXT = (By.CSS_SELECTOR, "#messages > .alert-success > .alertinner")

    @allure.step("Check success message presented")
    def should_be_success_message(self) -> None:
        assert self.is_element_present(self.SUCCESS_MESSAGE_TEXT), "Success message is not presented"

    @allure.step("Geet success message text")
    def get_success_message_text(self) -> str:
        return self.get_text(self.SUCCESS_MESSAGE_TEXT)
