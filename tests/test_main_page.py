import pytest
import allure


@pytest.mark.main_page
class TestMainPage:

    @pytest.mark.smoke
    @allure.title("Guest should see login link on main page")
    def test_guest_should_see_login_link(self, main_page):
        main_page.open()
        main_page.navbar.should_be_login_link()

    @pytest.mark.smoke
    @allure.title("Guest can go to login page from main page")
    def test_guest_can_go_to_login_page(self, main_page, login_page):
        main_page.open()
        main_page.navbar.go_to_login_page()
        login_page.should_be_login_url()
        login_page.should_be_login_page()

    @pytest.mark.smoke
    @allure.title("Guest cannot see product in cart opened from main page")
    def test_guest_cant_see_product_in_cart_opened_from_main_page(self, main_page, cart_page):
        main_page.open()
        main_page.navbar.go_to_cart_page()
        cart_page.should_be_cart_page_header()
        cart_page.should_be_continue_shopping_link()



