import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage

class CartPage(BasePage):
    path = 'catalogue/'

    CART_PAGE_HEADER_TEXT = (By.CSS_SELECTOR, ".page-header.action")
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner > p > a")
    GOODS_LIST = (By.CSS_SELECTOR, "div.basket_items > div.row > div")

    @allure.step("Check cart page header is present")
    def should_be_cart_page_header(self):
        assert self.is_element_present(self.CART_PAGE_HEADER_TEXT), "Cart page header not found"

    @allure.step("Check continue shopping link is present")
    def should_be_continue_shopping_link(self):
        assert self.is_element_present(self.CONTINUE_SHOPPING_LINK), "Continue shopping link not found"

    @allure.step("Go to main page using continue shopping link")
    def go_to_main_page_using_continue_shopping_link(self):
        self.click_element(self.CONTINUE_SHOPPING_LINK)

    @allure.step("Get list of goods")
    def get_list_of_goods(self) -> list:
        return self.get_list_of_elements(self.GOODS_LIST, timeout=2)
