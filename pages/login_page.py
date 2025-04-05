from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")  # Message d'erreur visible
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def enter_username(self, username):
        self.enter_text(*self.username_input, username)

    def enter_password(self, password):
        self.enter_text(*self.password_input, password)

    def click_login(self):
        self.click_element(*self.login_button)

    def get_error_message(self):
        return self.get_text(*self.error_message)

    def logout(self):
        self.click_element(*self.menu_button)
        self.click_element(*self.logout_link)
