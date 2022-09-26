from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url()
        assert "login" in current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM)

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.click()
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.click()
        password_field.send_keys(password)
        repeat_field = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        repeat_field.click()
        repeat_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        button.click()

    def login_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button.click()

    def should_success_reg_notice(self):
        assert self.is_element_present(*LoginPageLocators.REG_SUCCESS)
