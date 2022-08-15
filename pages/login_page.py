from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "ZAQ!1qaz"
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_password.send_keys(password)
        input_confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        input_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()