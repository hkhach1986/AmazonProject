import time
import unittest

from selenium import webdriver
from pages.signInPage import SignInPage
from pages.navigationBar import NavigationBar

class SignOutTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.signInPageObject = SignInPage(self.driver)
        self.__navigationBarObject = NavigationBar(self.driver)
        self.__titleBeforeLogin = self.signInPageObject.get_sign_in_title_element()
        self.assertEqual(self.__titleBeforeLogin.text, "Sign in", "We are not on Sign In Page")
        self.signInPageObject.fill_login_field("hkhach1985@gmail.com")
        self.signInPageObject.click_to_continue_button()
        time.sleep(2)
        self.signInPageObject.fill_password_field("Dzmer2025@")
        self.signInPageObject.click_to_sign_in_button()

    def test_to_sign_out(self):

        self.__navigationBarObject.mouse_move_to_user_profile()
        time.sleep(2)
        self.__navigationBarObject.sign_out_button()
        time.sleep(10)
        self.__titleAfterLogout = self.signInPageObject.get_sign_in_title_element()
        self.assertEqual(self.__titleAfterLogout.text, "Sign in", "We are not on Sign In Page")

    def tearDown(self):
        self.driver.close()