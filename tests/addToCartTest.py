import time
import unittest

from selenium import webdriver
from pages.signInPage import SignInPage
from pages.searchResultPage import SearchResultPage
from pages.navigationBar import NavigationBar
from pages.productDetailsPage import ProductDetailsPage
from selenium.webdriver.common.by import By
from pages.cartPage import CartPage

class AddToCartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.signInPageObject = SignInPage(self.driver)
        self.__navigationBarObject = NavigationBar(self.driver)
        self.__searchResulObject = SearchResultPage(self.driver)
        self.__productDetailsPageObject = ProductDetailsPage(self.driver)
        self.__cartPageObj = CartPage(self.driver)

    def test_add_to_cart(self):
        self.signInPageObject.fill_login_field("hkhach1985@gmail.com")
        self.signInPageObject.click_to_continue_button()
        time.sleep(2)
        self.signInPageObject.fill_password_field("Dzmer2025@")
        self.signInPageObject.click_to_sign_in_button()
        time.sleep(2)
        # assert (self.__navigationBarObject.get_account_list_user_name(), self.driver.find_element(By.XPATH, "//a[@aria-label = 'Amazon']").text, "Not found")
        time.sleep(10)
        self.__navigationBarObject.fill_search_field("Agv K5")
        self.__navigationBarObject.click_to_search_button()
        # self.__searchResulObject.click_add_to_cart_button()
        self.__searchResulObject.click_to_first_product()
        prductName = self.__productDetailsPageObject.get_product_name()
        self.__productDetailsPageObject.click_add_to_cart_from_product_detail_page_button()
        self.__navigationBarObject.click_to_cart_button()
        self.assertTrue(self.__cartPageObj.is_name_exist_in_cart(prductName))
        time.sleep(10)


    def tearDown(self):
        # self.__productDetailsPageObject.click_to_delete_added_product_from_cart_list()
        # time.sleep(5)
        self.driver.close()
