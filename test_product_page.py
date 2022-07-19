from .pages.product_page import ProductPage
from .pages.main_page import MainPage
import pytest

@pytest.mark.parametrize('promo_number', [i for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    if promo_number == 7:
        pytest.xfail()
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_message_of_product_adding()
    product_page.should_be_message_of_basket_value()

