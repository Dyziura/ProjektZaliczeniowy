from Tests.base_test import BaseTest
from time import sleep
from Test_data.csv_reader import get_test_data
import random
import unittest

class CartTest(BaseTest):
    
    def setUp(self):
        super().setUp() #wywołanie z klasy nadrzędnej z base_test.py
        # 1. Załadowanie strony catalogu
        self.catalog_page = self.home_page.click_enter_button()
    
    def test_TC_00001_AddingFishProductToCart(self):
        """TC_00001: Dodanie losowego produktu z kategorii Ryby do koszyka"""
        print("TC_00001: Dodanie losowego produktu z kategorii Ryby do koszyka")
        from Pages.cart_page import CartPage
        # 1. Przejdź do listy ryb
        self.catalog_page.go_to_fish_list()
        # 2. Przejdź do konkretnego gatunku ryb
        self.catalog_page.click_random_product_id()
        # 3. Dodaj do koszyka dowolną rybę
        added_item_id = self.catalog_page.add_random_item_to_cart2()
        self.cart_page = CartPage(self.driver)
        # 4. Pobierz listę produktów w koszyku
        item_ids = self.cart_page.get_all_item_ids_in_cart()
        #print(item_ids) #do weryfikacji czy działa
        #print(added_item_id)
        # 5. Sprawdź, czy dodany produkt znajduje się na liście produktów w koszyku
        self.assertIn(added_item_id, item_ids)

    def test_TC_00002_AddingDogsProductToCart(self):
        """TC_00002: Dodanie losowego produktu z kategorii Psy do koszyka"""
        print("TC_00002: Dodanie losowego produktu z kategorii Psy do koszyka")
        from Pages.cart_page import CartPage
        from Pages.catalog_page import CatalogPageLocators
        # 1. Przejdź do listy psów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.dogsList)
        # 2. Przejdź do konkretnego gatunku psów
        self.catalog_page.click_random_product_id()
        # 3. Dodaj do koszyka dowolnego psa
        added_item_id = self.catalog_page.add_random_item_to_cart2()
        self.cart_page = CartPage(self.driver)
        # 4. Pobierz listę produktów w koszyku
        item_ids = self.cart_page.get_all_item_ids_in_cart()
        # 5. Sprawdź, czy dodany produkt znajduje się na liście produktów w koszyku
        self.assertIn(added_item_id, item_ids)

    def test_TC_00003_AddingCatsProductToCart(self):
        """TC_00003: Dodanie losowego produktu z kategorii Koty do koszyka"""
        print("TC_00003: Dodanie losowego produktu z kategorii Koty do koszyka")
        from Pages.cart_page import CartPage
        from Pages.catalog_page import CatalogPageLocators
        # 1. Przejdź do listy kotów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.catsList)
        # 2. Przejdź do konkretnego gatunku kotów
        self.catalog_page.click_random_product_id()
        # 3. Dodaj do koszyka dowolnego kota
        added_item_id = self.catalog_page.add_random_item_to_cart2()
        self.cart_page = CartPage(self.driver)
        # 4. Pobierz listę produktów w koszyku
        item_ids = self.cart_page.get_all_item_ids_in_cart()
        # 5. Sprawdź, czy dodany produkt znajduje się na liście produktów w koszyku
        self.assertIn(added_item_id, item_ids)

    @unittest.skip("Tymczasowo wylaczony test. Wymaga dopracowania") #przykład użycia dekoratora do pominięcia testu
    def test_TC_00004_UpdatingQuantityOfItemInCart(self):
        """TC_00004: Aktualizacja ilości produktu w koszyku"""
        print("TC_00004: Aktualizacja ilości produktu w koszyku")
        from Pages.cart_page import CartPage
        # 1. Przejdź do listy ryb
        self.catalog_page.go_to_fish_list()
        # 2. Przejdź do konkretnego gatunku ryb
        self.catalog_page.click_random_product_id()
        # 3. Dodaj do koszyka dowolną rybę
        added_item_id = self.catalog_page.add_random_item_to_cart2()
        self.cart_page = CartPage(self.driver)
        # 4. Pobierz pole z ilością produktu w koszyku
        quantity_field = self.cart_page.get_quantity_of_item_in_cart(added_item_id)
        # 5. Ustaw nową ilość produktu w koszyku
        new_quantity = random.randint(1, 10)
        sleep(5)

    def test_TC_00005_AddingReptilesProductToCart(self):
        """TC_00005: Dodanie losowego produktu z kategorii Gady do koszyka"""
        print("TC_00005: Dodanie losowego produktu z kategorii Gady do koszyka")
        from Pages.cart_page import CartPage
        from Pages.catalog_page import CatalogPageLocators
        # 1. Przejdź do listy gadów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.reptilesList)
        # 2. Przejdź do konkretnego gatunku gadów
        self.catalog_page.click_random_product_id()
        # 3. Dodaj do koszyka dowolnego gada
        added_item_id = self.catalog_page.add_random_item_to_cart2()
        self.cart_page = CartPage(self.driver)
        # 4. Pobierz listę produktów w koszyku
        item_ids = self.cart_page.get_all_item_ids_in_cart()
        # 5. Sprawdź, czy dodany produkt znajduje się na liście produktów w koszyku
        self.assertIn(added_item_id, item_ids) #added_item_id to wartość, której szukamy na liście item_ids
    
    def test_TC_00006_AddingBirdsProductToCart(self):
        """TC_00006: Dodanie losowego produktu z kategorii Ptaki do koszyka"""
        print("TC_00006: Dodanie losowego produktu z kategorii Ptaki do koszyka")
        from Pages.cart_page import CartPage
        from Pages.catalog_page import CatalogPageLocators
        # 1. Przejdź do listy ptaków
        self.catalog_page.go_to_animal_list(CatalogPageLocators.birdsList)
        # 2. Przejdź do konkretnego gatunku ptaków
        self.catalog_page.click_random_product_id()
        # 3. Dodaj do koszyka dowolnego ptaka
        added_item_id = self.catalog_page.add_random_item_to_cart2()
        self.cart_page = CartPage(self.driver)
        # 4. Pobierz listę produktów w koszyku
        item_ids = self.cart_page.get_all_item_ids_in_cart()
        # 5. Sprawdź, czy dodany produkt znajduje się na liście produktów w koszyku
        self.assertIn(added_item_id, item_ids)