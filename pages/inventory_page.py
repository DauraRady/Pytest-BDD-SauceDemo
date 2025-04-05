from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from pages.cart_page import CartPage

class InventoryPage(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")

    def get_cart_count(self):
        return int(self.find_element(*self.CART_COUNT).text)

    def sort_products_high_to_low(self):
        dropdown = Select(self.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_value("hilo")  # High to Low

    def add_top_two_products_to_cart(self):
        buttons = self.find_elements(*self.ADD_TO_CART_BUTTONS)
        for i in range(min(2, len(buttons))):
            buttons[i].click()

    def go_to_cart(self):
        self.click_element(*self.CART_ICON)
        return CartPage(self.driver)
