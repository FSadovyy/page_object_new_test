from .base_page import BasePage
from .locators import MainPageLocators

class LoginPage(BasePage):
    url = self.driver.current_url

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url == MainPageLocators.LOGIN_URL, "Login url is wrong"

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not presented"
