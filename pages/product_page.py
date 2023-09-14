from .base_page import BasePage
from .locators import MainPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_cart_button()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*MainPageLocators.ADD_TO_CART_BUTTON), "Add button is not presented"

    def add_product_in_cart(self):
        product_button = self.browser.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
        product_button.click()
