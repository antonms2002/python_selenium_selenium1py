from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
import math
import allure

class ProductPage(BasePage):
    # default good path
    path = 'catalogue/coders-at-work_207/?promo=newYear2019'

    # locators
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket.btn-primary ")
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, "div.product_main > h1")
    DESCRIPTION_TITLE_TEXT = (By.ID, "product_description")
    ADD_TO_CART_SUCCESS_MESSAGE_DIV = (By.CLASS_NAME, "div.alertinner")
    ADD_TO_CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    UNAVAILABILITY_TEXT = (By.CSS_SELECTOR, "div.product_main .outofstock.availability")
    PRICE_TEXT = (By.CSS_SELECTOR, "p.price_color")

    def open(self, path = None) -> None:
        if path is None:
            path = self.path
        super().open(path)

    @allure.step("Check product title is present")
    def should_be_product_title(self) -> None:
        assert self.is_element_present(self.PRODUCT_NAME_TEXT), "Product name was not found."

    @allure.step("Add product to cart")
    def add_to_cart(self) -> None:
        self.click_element(self.ADD_TO_CART_BUTTON)

    @allure.step("Check add to cart button is not present (unavailable goods)")
    def should_not_be_add_to_cart(self) -> None:
        assert self.is_not_element_present(self.ADD_TO_CART_BUTTON), "Add to cart button was found."

    @allure.step("Get product title text")
    def get_product_title_text(self) -> str:
        return self.get_text(self.PRODUCT_NAME_TEXT)

    @allure.step("Get product price text")
    def get_product_price_text(self) -> str:
        return self.get_text(self.PRICE_TEXT)

    @allure.step("Check product title and price match expected values")
    def should_be_right_title_and_price(self, expected_product_title: str, expected_price: str) -> None:
        product_title = self.get_product_title_text()
        price = self.get_product_price_text()
        assert product_title == expected_product_title, f"Expected: {expected_product_title}, Actual: {product_title}"
        assert price == expected_price, f"Expected: {expected_price}, Actual: {price}"

    @allure.step("Get add to cart success message text")
    def get_add_to_cart_success_message_text(self) -> str:
        return self.get_text(self.ADD_TO_CART_SUCCESS_MESSAGE)

    @allure.step("Check success message is not present")
    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(self.ADD_TO_CART_SUCCESS_MESSAGE_DIV), "Success message was found."

    @allure.step("Check success message disappears")
    def should_disappear_success_message(self) -> None:
        assert self.is_element_disappeared(self.ADD_TO_CART_SUCCESS_MESSAGE_DIV), "Success message is not disappeared."

    @allure.step("Check product name matches success message")
    def should_be_same_text_product_name_and_success_message(self) -> None:
        assert self.get_product_title_text() == self.get_add_to_cart_success_message_text(), \
            "Product name in success message is different than product name"

    @allure.step("Check unavailability message is present")
    def should_be_unavailability_message(self) -> None:
        assert self.is_element_present(self.UNAVAILABILITY_TEXT), "No unavailability message was found."

    @allure.step("Solve quiz and get code from alert")
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


