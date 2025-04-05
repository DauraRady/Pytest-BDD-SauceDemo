
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC



class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRMATION_TEXT = (By.CLASS_NAME, "complete-header")

    def enter_shipping_info(self, first_name, last_name, postal_code):
        self.enter_text(*self.FIRST_NAME, first_name)
        self.enter_text(*self.LAST_NAME, last_name)
        self.enter_text(*self.POSTAL_CODE, postal_code)
        self.click_element(*self.CONTINUE_BUTTON)

    def finalize_order(self):
        self.click_element(*self.FINISH_BUTTON)
    def get_confirmation_message(self):
        self.wait.until(EC.presence_of_element_located(self.CONFIRMATION_TEXT))
        return self.find_element(*self.CONFIRMATION_TEXT).text
    