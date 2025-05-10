from Pages.base_page import BasePage
from Pages.sign_in_page import SignInPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CatalogPageLocators:
    """
    Catalog Page locators
    """
    searchField = (By.CSS_SELECTOR, 'input[name="keyword"]') #Page Object naming convention
    searchButton = (By.CSS_SELECTOR, 'input[value="Search"]')
    searchMessage = (By.CSS_SELECTOR, '#Content ul.messages:nth-of-type(1) li:first-child')
    nameProduct = (By.CSS_SELECTOR, '#Catalog > table > tbody > tr:nth-child(2) > td:nth-child(3)')
    signIn = (By.CSS_SELECTOR, 'a[href="/actions/Account.action?signonForm="]')
    returnToMainMenu = (By.CSS_SELECTOR, '#BackLink > a')
    bodyMain = (By.CSS_SELECTOR, '#Main')


class CatalogPage(BasePage):
    """
    Catalog Page Object
    """
    def enter_search_value(self, search_value):
        """
        Enter search value
        """
        # 1. Znajdź pole szukaj
        # 2. Kliknij w pole
        self.driver.find_element(*CatalogPageLocators.searchField).click()
        # 3. Wpisz wartość
        self.driver.find_element(*CatalogPageLocators.searchField).send_keys(search_value)
        # 4. Kliknij Search
        self.driver.find_element(*CatalogPageLocators.searchButton).click()

    def get_alert_message(self):
        """
        Get alert message
        """
        # 1. Znajdź alert
        # 2. Zwróć tekst alertu
        return self.driver.find_element(*CatalogPageLocators.searchMessage).text
    
    def get_name_product(self):
        """
        Get name product
        """
        # 1. Znajdź nazwę produktu
        # 2. Zwróć tekst produktu
        return self.driver.find_element(*CatalogPageLocators.nameProduct).text
    
    def sign_in_button(self):
        """
        Click Sign In button
        """
        # 1. Znajdź przycisk Sign In
        el = self.driver.find_element(*CatalogPageLocators.signIn)
        # 2. Kliknij w przycisk
        el.click()
        # Zwróć stronę logowania
        return SignInPage(self.driver)
    
    def return_to_main_menu(self):
        """
        Click Return to Main Menu button
        """
        # 1. Znajdź przycisk Return to Main Menu
        el = self.driver.find_element(*CatalogPageLocators.returnToMainMenu)
        # 2. Kliknij w przycisk
        el.click()
        # Zwróć stronę logowania
        return CatalogPage(self.driver)
    
    def is_Catalog_Page(self):
        """
        Confirm presence of Catalog Page
        """
        # 1. Sprawdź, czy jesteś na stronie katalogu
        return self.driver.find_element(*CatalogPageLocators.bodyMain).is_displayed()