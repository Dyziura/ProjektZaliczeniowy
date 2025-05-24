from Pages.base_page import BasePage
from Pages.sign_in_page import SignInPage
from Pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random

class CatalogPageLocators:
    """
    Catalog Page locators
    """
    searchField = (By.CSS_SELECTOR, 'input[name="keyword"]') #Page Object naming convention
    searchButton = (By.CSS_SELECTOR, 'input[value="Search"]')
    searchMessage = (By.CSS_SELECTOR, '#Content ul.messages:nth-of-type(1) li:first-child')
    nameProduct = (By.CSS_SELECTOR, '#Catalog > table > tbody > tr:nth-child(2) > td:nth-child(3)')
    signIn = (By.LINK_TEXT, 'Sign In')
    cartButton = (By.CSS_SELECTOR, 'img[name="img_cart"]') #link do koszyka
    #signIn = (By.CSS_SELECTOR, 'a[href="/actions/Account.action?signonForm="]')
    returnToMainMenu = (By.CSS_SELECTOR, '#BackLink > a')
    bodyMain = (By.CSS_SELECTOR, '#Main')
    birdsList = (By.CSS_SELECTOR, 'area[alt=Birds]') #link portretowy do listy ptaków
    fishList = (By.CSS_SELECTOR, 'area[alt=Fish]') #link portretowy do listy ryb
    dogsList = (By.CSS_SELECTOR, 'area[alt=Dogs]') #link portretowy do listy psów
    reptilesList = (By.CSS_SELECTOR, 'area[alt=Reptiles]') #link portretowy do listy gadów
    catsList = (By.CSS_SELECTOR, 'area[alt=Cats]') #link portretowy do listy kotów
    birdsList2 = (By.CSS_SELECTOR, 'img[src*="birds"]') #link napis do listy ptaków - pod koszykiem
    fishList2 = (By.CSS_SELECTOR, 'img[src*="fish"]') #link napis do listy ryb - pod koszykiem
    dogsList2 = (By.CSS_SELECTOR, 'img[src*="dogs"]') #link napis do listy psów - pod koszykiem
    reptilesList2 = (By.CSS_SELECTOR, 'img[src*="reptiles"]') #link napis do listy gadów - pod koszykiem
    catsList2 = (By.CSS_SELECTOR, 'img[src*="cats"]') #link napis do listy kotów - pod koszykiem
    birdsList3 = (By.CSS_SELECTOR, 'img[src*="birds_icon"]') #link napis z opisem do listy ptaków
    fishList3 = (By.CSS_SELECTOR, 'img[src*="fish_icon"]') #link napis z opisem do listy ryb
    dogsList3 = (By.CSS_SELECTOR, 'img[src*="dogs_icon"]') #link napis z opisem do listy psów
    reptilesList3 = (By.CSS_SELECTOR, 'img[src*="reptiles_icon"]') #link napis z opisem do listy gadów
    catsList3 = (By.CSS_SELECTOR, 'img[src*="cats_icon"]') #link napis z opisem do listy kotów
    randomAnimalFromList = (By.CSS_SELECTOR, 'a[href*="productId"]') #* to match productId with any value after it and before it
    randomItemFromList = (By.CSS_SELECTOR, 'a[href*="workingItemId=EST-"]') #oznacza, że szukamy linków zawierających "workingItemId=EST-"
    randomTableRow = (By.CSS_SELECTOR, 'table tr') #zwraca wiersze tabeli
    tableRowsWithItemId = (By.CSS_SELECTOR, 'a[href*="viewItem"]') #szukamy wierszy zawierających "viewItem" w tabeli
    titleAnimalList = (By.CSS_SELECTOR, '#Catalog > h2') #szukamy tytułu listy zwierząt

class CatalogPageVariables:
    """
    Catalog Page Variables
    """
    infoMessageSearchField = "Please enter a keyword to search for, then press the search button."
    titleCatsList = "Cats" 
    titleFishList = "Fish"
    titleDogsList = "Dogs"
    titleReptilesList = "Reptiles"
    titleBirdsList = "Birds"

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
    
    def get_title_animal_list(self):
        """
        Get title list of animals
        """
        # 1. Znajdź nazwę produktu
        # 2. Zwróć tekst produktu
        return self.driver.find_element(*CatalogPageLocators.titleAnimalList).text
    
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
    
    def cart_button(self):
        """
        Click Cart button
        """
        # 1. Znajdź przycisk Sign In
        el = self.driver.find_element(*CatalogPageLocators.cartButton)
        # 2. Kliknij w przycisk
        el.click()
        # Zwróć stronę logowania
        return CartPage(self.driver)
    
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
    
    def go_to_fish_list(self):
        """
        Go to fish list
        """
        # 1. Otwiera listę ryb
        self.driver.find_element(*CatalogPageLocators.fishList).click()

    def go_to_animal_list(self, animalLocator):
        """
        Go to animal list
        """
        # sprawdzenie metody
        #print(f"Klikam w: {animalLocator}")
        # 1. Otwiera listę kotów
        self.driver.find_element(*animalLocator).click()
    
    def click_random_product_id(self):
        """
        Click random product id
        """
        # 1. Znajdź wszystkie elementy z atrybutem name zaczynającym się od "EST-"
        inputs = self.driver.find_elements(*CatalogPageLocators.randomAnimalFromList)
        # 2. Wybierz losowy element z listy
        random_input = random.choice(inputs)
        # 3. Kliknij w losowy element
        random_input.click()

    def add_random_item_to_cart(self):
        """
        Add random item to cart
        """
        # 1. Znajdź wszystkie elementy z atrybutem name zaczynającym się od "EST-"
        inputs = self.driver.find_elements(*CatalogPageLocators.randomItemFromList)
        # 2. Wybierz losowy element z listy
        random_input = random.choice(inputs)
        # 3. Pobierz tekst z np. <a href="/actions/Catalog.action?viewItem=&amp;itemId=EST-1">EST-1</a> ---> EST-1
        item_id = random_input.text
        # 4. Kliknij w losowy element
        random_input.click()
        return item_id
    
    def add_random_item_to_cart2(self):
        """
        Find random item from table, extract its item ID (ex. EST-1) and add to cart
        """
        # 1. Znajdź wszystkie elementy tabeli
        rows = self.driver.find_elements(*CatalogPageLocators.randomTableRow)
        # 2. Filtrowanie wierszy, aby znaleźć te, które zawierają elementy z tekstem "viewItem" - tworzy listę
        valid_rows = [row for row in rows if row.find_elements(*CatalogPageLocators.tableRowsWithItemId)]
        # 3. Wybierz losowy wiersz z listy
        random_row = random.choice(valid_rows)
        # 4. Pobierz item ID z np. <a href="/actions/Catalog.action?viewItem=&amp;itemId=EST-1">EST-1</a> ---> EST-1
        item_link = random_row.find_element(*CatalogPageLocators.tableRowsWithItemId)
        item_id = item_link.text.strip()  # strip() usuwa ewentualne białe znaki na początku i końcu
        # 5. Kliknij w przycisk "Add to Cart" w tym samym wierszu
        add_to_cart_button = random_row.find_element(*CatalogPageLocators.randomItemFromList)
        add_to_cart_button.click()
        # 6. Zwróć item ID
        return item_id
    
    def is_Catalog_Page(self):
        """
        Confirm presence of Catalog Page
        """
        # 1. Sprawdź, czy jesteś na stronie katalogu
        return self.driver.find_element(*CatalogPageLocators.bodyMain).is_displayed()