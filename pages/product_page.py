from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()
        
    def should_be_message_of_product_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product = self.browser.find_element(*ProductPageLocators.MESSAGE_OF_PRODUCT_ADDING).text
        assert product_name == message_product, "Name of product isn't matched"
        
    def should_be_message_of_basket_value(self):
        message_value = self.browser.find_element(*ProductPageLocators.MESSAGE_OF_BASKET_VALUE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_value, "Price in the basket and in the message isn't matched"
