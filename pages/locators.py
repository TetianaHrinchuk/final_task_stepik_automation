from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    MESSAGE_OF_PRODUCT_ADDING = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner>strong")
    MESSAGE_OF_BASKET_VALUE = (By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    