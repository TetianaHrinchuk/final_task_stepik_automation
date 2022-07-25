from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_item(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ITEM), \
       "Product item is presented, but should not be"
    def should_be_message_of_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert "empty" in text, \
       "Not correct message about empty basket"

    