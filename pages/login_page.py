import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .main_page import MainPage


class LoginPage(BasePage):
    # URL path Login page
    path = 'accounts/login/'
    # locators
    LOGIN_EMAIL_FIELD = (By.ID, "id_login-username")
    LOGIN_PASSWORD_FIELD = (By.ID, "id_login-password")
    LOGIN_FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "[href$='/password-reset/']")
    LOGIN_ENTER_BUTTON = (By.NAME, "login_submit")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_REPEAT_FIELD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

    def open(self, path = None) -> None:
        super().open(path=self.path)

    @allure.step("Check login page is displayed correctly")
    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step("Check login page URL")
    def should_be_login_url(self) -> None:
        current_url = self.get_url()
        assert self.path in current_url, \
            f"Login page url does not match login page url. Actual: {self.browser.current_url}"

    @allure.step("Check login form elements are present")
    def should_be_login_form(self):
        assert self.is_element_present(self.LOGIN_EMAIL_FIELD), "Login email field is not presented."
        assert self.is_element_present(self.LOGIN_PASSWORD_FIELD), "Login password field is not presented."
        assert self.is_element_present(self.LOGIN_FORGOT_PASSWORD_LINK), "Login forgot password field is not presented."
        assert self.is_element_present(self.LOGIN_ENTER_BUTTON), "Login enter button is not presented."

    @allure.step("Check registration form elements are present")
    def should_be_register_form(self):
        assert self.is_element_present(self.REGISTER_EMAIL_FIELD), "Registration email field is not presented."
        assert self.is_element_present(self.REGISTER_PASSWORD_FIELD), "Registration password field is not presented."
        assert self.is_element_present(self.REGISTER_PASSWORD_REPEAT_FIELD), "Registration password repeat field is not presented."
        assert self.is_element_present(self.REGISTER_BUTTON), "Registration button is not presented."

    @allure.step("Fill sign up form with valid data. email: {email}, password: {password}, repeat_password: {repeat_password:}")
    def fill_sign_up_form_valid_data(self, email: str, password: str, repeat_password: str) -> MainPage:
        self.enter_text(self.REGISTER_EMAIL_FIELD, email)
        self.enter_text(self.REGISTER_PASSWORD_FIELD, password)
        self.enter_text(self.REGISTER_PASSWORD_REPEAT_FIELD, repeat_password)
        self.click_element(self.REGISTER_BUTTON)
        return MainPage(self.browser)