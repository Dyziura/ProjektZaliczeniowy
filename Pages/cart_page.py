from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPageLocators:
    """
    Cart Page locators
    """
    returnToMainMenu = (By.CSS_SELECTOR, '#BackLink > a') #Page Object naming convention / taki sam locator jak w CatalogPage
    updateCartButton = (By.CSS_SELECTOR, 'input[name="updateCartQuantities"]') #Page Object naming convention
    bodyCart = (By.CSS_SELECTOR, '#Cart') #Page Object naming convention
    
class CartPageVariables:
    """
    Cart Page Variables
    """
    invalidUsernamePassword = "Invalid username or password. Signon failed."

class CartPage(BasePage):
    """
    Cart Page Object
    """
    def get_all_item_ids_in_cart(self):
        """
        Lists of all item ids in cart
        """
        # 1. Znajdź wszystkie inputy z atrybutem name zaczynającym się od "EST-"
        inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[name^="EST-"]') #input[name^="EST-" oznacza, że szukamy inputów, których name zaczyna się od "EST-"
        # 2. Utwórz listę atrybutów name
        item_ids = [inp.get_attribute('name') for inp in inputs] #inp.get_attribute('name') zwraca wartość atrybutu name
        # 3. Zwróć listę
        return item_ids
    
    def get_quantity_of_item_in_cart(self, item_id):
        """
        Field with quantity for item in cart
        """
        # 1. Znajdź pole do wprowadzenia ilości
        el = self.driver.find_element(By.CSS_SELECTOR, f'input[name="{item_id}"]') #f-string tworzenie stringa ze zmienną item_id
        # 2. Zwróć wartość
        return el

    def set_quantity_for_item_in_cart(self, item_id, quantity):
        """
        Set quantity for item in cart
        """
        field = self.get_quantity_of_item_in_cart(item_id) #pobranie pola z ilością
        # 1. Wyczyść pole
        field.clear()
        # 2. Wpisz wartość
        field.send_keys(str(quantity)) #str(quantity) zamienia liczbę na stringa, aby można było wpisać w pole

    def click_return_to_main_menu_button(self):
        from Pages.catalog_page import CatalogPage
        """
        Click return to main menu button
        """
        # 1. Znajdź przycisk Login
        el = self.driver.find_element(*CartPageLocators.returnToMainMenu)
        # 2. Kliknij w przycisk
        el.click()
        # Zwróć stronę katalogu
        return CatalogPage(self.driver)
    
    def click_update_cart_button(self):
        """
        Click update cart button
        """
        # 1. Znajdź przycisk Login
        el = self.driver.find_element(*CartPageLocators.updateCartButton)
        # 2. Kliknij w przycisk
        el.click()
    
    def is_Cart_Page(self):
        """
        Confirm presence of Cart Page
        """
        # 1. Sprawdź, czy jesteś na stronie koszyka
        return self.driver.find_element(*CartPageLocators.bodyCart).is_displayed()

#print(SignInPageVariables.invalidUsernamePassword) #do weryfikacji czy działa