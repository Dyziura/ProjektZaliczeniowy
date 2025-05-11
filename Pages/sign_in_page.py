from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPageLocators:
    """
    Sign In Page locators
    """
    usernameInput = (By.CSS_SELECTOR, 'input[name="username"]') #Page Object naming convention
    passwordInput = (By.CSS_SELECTOR, 'input[name=password]') #Page Object naming convention
    loginButton = (By.CSS_SELECTOR, 'input[value="Login"]') #Page Object naming convention
    loginMessage = (By.CSS_SELECTOR, '#Content ul.messages:nth-of-type(1) li:first-child') #Page Object naming convention

class SignInPageVariables:
    """
    Sign In Page Variables
    """
    invalidUsernamePassword = "Invalid username or password. Signon failed."

class SignInPage(BasePage):
    """
    Sign In Page Object
    """
    def type_in_username(self, username_value):
        #from Pages.catalog_page import CatalogPage # Import CatalogPage here to avoid circular import
        """
        Type in username
        """
        # 1. Znajdź pole do wprowadzenia imienia/loginu
        # 2. Kliknij w pole
        self.driver.find_element(*SignInPageLocators.usernameInput).click()
        # 3. Wpisz wartość
        self.driver.find_element(*SignInPageLocators.usernameInput).send_keys(username_value)

    def type_in_password(self, password_value):
        """
        Type in password
        """
        # 1. Znajdź pole do wprowadzenia hasła
        # 2. Kliknij w pole
        self.driver.find_element(*SignInPageLocators.passwordInput).click()
        # 3. Wpisz wartość
        self.driver.find_element(*SignInPageLocators.passwordInput).send_keys(password_value)

    def click_login_button(self):
        """
        Click login button
        """
        # 1. Znajdź przycisk Login
        el = self.driver.find_element(*SignInPageLocators.loginButton)
        # 2. Kliknij w przycisk
        el.click()

    def get_alert_message(self):
        """
        Get alert message
        """
        # 1. Znajdź alert
        # 2. Zwróć tekst alertu
        return self.driver.find_element(*SignInPageLocators.loginMessage).text

#print(SignInPageVariables.invalidUsernamePassword) #do weryfikacji czy działa
