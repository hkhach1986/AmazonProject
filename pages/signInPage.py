from selenium import webdriver
from selenium.webdriver.common.by import By

class SignInPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.__loginFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signInButtonLocator = (By.ID, "signInSubmit")


    def fill_login_field(self, login):
        loginFieldElement = self.driver.find_element(*self.__loginFieldLocator)
        loginFieldElement.send_keys(login)

    def click_to_continue_button(self):
        continueButtonElement = self.driver.find_element(*self.__continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password):
        passwordFielcElement = self.driver.find_element(*self.__passwordFieldLocator)
        passwordFielcElement.send_keys(password)

    def click_to_sign_in_button(self):
        signInButtonElement = self.driver.find_element(*self.__signInButtonLocator)
        signInButtonElement.click()
