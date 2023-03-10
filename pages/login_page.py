from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, 'URL NO'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.is_element_present(*MainPageLocators.LOGIN_FORM)
        assert login_form, 'There is no login form'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.REGISTR_FORM), 'There is no registration form'
