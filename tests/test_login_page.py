import pytest
import allure
import uuid

class TestLoginPage:

    @allure.title("Sign up with valid data")
    @pytest.mark.smoke
    def test_sign_up_with_valid_data(self, login_page, fake):
        email = fake.email()
        #email = f"{str(uuid.uuid1())[:9]}@gmail.com"
        password = fake.password()

        login_page.open()
        login_page.should_be_register_form()
        main_page = login_page.fill_sign_up_form_valid_data(email=email, password=password, repeat_password=password)
        main_page.should_be_success_message()
