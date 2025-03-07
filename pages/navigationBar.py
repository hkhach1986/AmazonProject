from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class NavigationBar():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.action = ActionChains(driver)
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__amazonIconButtonLocator = (By.ID, "nav-logo-sprites")
        self.__accountListHoverLocator = (By.ID, "nav-link-accountList")
        self.__signOutLocator = (By.XPATH, "//span[contains(text(),'Sign Out')]")
        self.__accountListUserNameLocator = (By.XPATH, "//a[@aria-label = 'Amazon']")
        self.__cartButtonLocator = (By.ID, "nav-cart")


    def fill_search_field(self, desiredItem):
        searchFieldElement = self.driver.find_element(*self.__searchFieldLocator)
        searchFieldElement.send_keys(desiredItem)

    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(*self.__searchButtonLocator)
        searchButtonElement.click()

    def click_to_amazon_icon(self):
        amazonIconButtonElement = self.driver.find_element(*self.__amazonIconButtonLocator)
        amazonIconButtonElement.click()

    def mouse_move_to_user_profile(self):
        acountListHoverElement = self.driver.find_element(*self.__accountListHoverLocator)
        self.action.move_to_element(acountListHoverElement).perform()

    def sign_out_button(self):
        #signOutButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*self.__signOutLocator))
        signOutButton = self.driver.find_element(*self.__signOutLocator)
        signOutButton.click()

    def get_account_list_user_name(self):
        accountListUserNameElement = self.driver.find_element(*self.__accountListUserNameLocator)
        return accountListUserNameElement.text

    def click_to_cart_button(self):
        cartButtonElement = self.driver.find_element(*(self.__cartButtonLocator))
        cartButtonElement.click()

