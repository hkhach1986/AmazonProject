from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SearchResultPage():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.__addToCartButtonLocator = (By.XPATH, "(//button[@name = 'submit.addToCart'])[2]")
        self.__firstProductLocator = (By.XPATH, "(//div[@class = 'a-section aok-relative s-image-square-aspect'])[2]")

    def click_add_to_cart_button(self):
        addToCartButtonElement = self.driver.find_element(*self.__addToCartButtonLocator)
        addToCartButtonElement.click()

    def click_to_first_product(self):
        firstProductElement = self.driver.find_element(*self.__firstProductLocator)
        firstProductElement.click()

