from Pages.base_page import BasePage
from Pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class HomePageLocators:
    """
    Home Page locators
    """
    enterTheStoreButton = (By.CSS_SELECTOR, 'a[href="actions/Catalog.action"]') #Page Object naming convention

class HomePage(BasePage):
    """
    Home Page Object
    """
    def click_enter_button(self):
        """
        Click enter button
        """
        # 1. Znajdź przycisk Enter the store
        el = self.driver.find_element(*HomePageLocators.enterTheStoreButton) # * to rozpakowanie krotki czyli *(By.ID, "login2") = By.ID, "login2"
        # 2. Kliknij w przycisk
        el.click()
        # Zwróć stronę katalogu
        return CatalogPage(self.driver)

