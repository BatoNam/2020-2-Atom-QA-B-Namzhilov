from ui.locators.locators import AuthPageLocators
from ui.pages.base_page import BasePage


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def auth(self, email, password):
        self.click(self.locators.AUTH_OPEN_BUTTON)
        self.placeholder_send_keys(self.locators.EMAIL_PLACEHOLDER, email)
        self.placeholder_send_keys(self.locators.PASSD_PLACEHOLDER, password)
        self.click(self.locators.LOGIN_BUTTON)
