import time
import unittest

from selenium import webdriver
from pages.signInPage import SignInPage

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.signInPageObject = SignInPage(self.driver)

    def test_positive_login(self):
        self.signInPageObject.fill_login_field("hkhach1985@gmail.com")
        self.signInPageObject.click_to_continue_button()
        time.sleep(2)
        self.signInPageObject.fill_password_field("Dzmer2025@")
        self.signInPageObject.click_to_sign_in_button()
        time.sleep(20)
    def tearDown(self):
        self.driver.close()
