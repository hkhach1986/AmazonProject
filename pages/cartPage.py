from selenium.webdriver.common.by import By

class CartPage():
    def __init__(self, driver):
        self.driver = driver
        self.__productsLocator = (By.XPATH, "//div[@class='a-row sc-list-item sc-java-remote-feature']")

    def get_all_product_elements(self):
        product_elements = self.driver.find_elements(*(self.__productsLocator))
        return product_elements

    def is_name_exist_in_cart(self, name):
        result = False
        productsThatContainCart = self.get_all_product_elements()
        for product in productsThatContainCart:
            if name in product.text:
                result = True
                continue

        return result
