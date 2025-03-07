from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductDetailsPage():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.__addToCartButtonFromProductDetailsPageLocator = (By.ID, "add-to-cart-button")
        self.__deleteAddedProductFromCartListLocator = (By.XPATH, "//button[@title = 'Delete 2 items']")
        self.__productNameLocator = (By.ID, "productTitle")

    def click_add_to_cart_from_product_detail_page_button(self):
        addToCartButtonElement = self.driver.find_element(*self.__addToCartButtonFromProductDetailsPageLocator)
        addToCartButtonElement.click()

    def click_to_delete_added_product_from_cart_list(self):
        deleteAddedProductFromCartListElement = self.driver.find_element(*self.__deleteAddedProductFromCartListLocator)
        deleteAddedProductFromCartListElement.click()

    def get_product_name(self):
        productNameElement = self.driver.find_element(*(self.__productNameLocator))
        return productNameElement.text