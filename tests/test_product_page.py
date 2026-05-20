import pytest
import allure

@pytest.mark.product_page
class TestProductPage:

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "path",
        ["catalogue/coders-at-work_207/?promo=offer0",
         "catalogue/coders-at-work_207/?promo=offer1",
         "catalogue/coders-at-work_207/?promo=offer2",
         "catalogue/coders-at-work_207/?promo=offer3",
         "catalogue/coders-at-work_207/?promo=offer4",
         "catalogue/coders-at-work_207/?promo=offer5",
         "catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
         "catalogue/coders-at-work_207/?promo=offer8",
         "catalogue/coders-at-work_207/?promo=offer9"],
        ids=["offer0", "offer1", "offer2", "offer3", "offer4",
             "offer5", "offer6", "offer7", "offer8", "offer9"])
    @allure.title("Guest can add product to basket")
    def test_guest_can_add_product_to_basket(self, product_page, path):
        product_page.open(path)
        product_page.should_be_product_title()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_same_text_product_name_and_success_message()

    @pytest.mark.smoke
    @allure.title("Guest should see login link on product page")
    def test_guest_should_be_login_link(self, product_page):
        product_page.open()
        product_page.navbar.should_be_login_link()

    @pytest.mark.smoke
    @allure.title("Guest can go to login page from product page")
    def test_guest_can_go_to_login_page_from_product_page(self, product_page, login_page):
        product_page.open()
        product_page.navbar.go_to_login_page()
        login_page.should_be_login_form()

    @pytest.mark.smoke
    @allure.title("Check unavailable product")
    def test_unavailable_good(self, product_page):
        product_page.open(path="catalogue/hackers-painters_185/")
        product_page.should_be_product_title()
        product_page.should_be_unavailability_message()
        product_page.should_not_be_add_to_cart()

    @pytest.mark.cp
    @allure.title("Guest cannot see success message without adding to cart")
    def test_guest_cant_see_success_message_without_adding_to_cart(self, product_page):
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.smoke
    @allure.title("Guest cannot see product in basket opened from product page")
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, product_page, cart_page):
        product_page.open()
        product_page.navbar.go_to_cart_page()
        cart_page.should_be_cart_page_header()
        cart_page.should_be_continue_shopping_link()
        assert not len(cart_page.get_list_of_goods()), "Cart is not empty"

    @pytest.mark.cp
    @pytest.mark.skip(reason="Not valid test. Made for page methods debug")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, product_page):
        product_page.open()
        product_page.add_to_cart()
        product_page.should_not_be_success_message()

    @pytest.mark.cp
    @pytest.mark.skip(reason="Not valid test. Made for page methods debug")
    def test_message_disappeared_after_adding_product_to_basket(self, product_page):
        product_page.open()
        product_page.add_to_cart()
        product_page.should_disappear_success_message()