from Tests.base_test import BaseTest
from time import sleep
from Test_data.csv_reader import get_test_data
import random

class CartTest(BaseTest):
    
    def setUp(self):
        super().setUp() #wywołanie z klasy nadrzędnej z base_test.py
        # 1. Załadowanie strony catalogu
        self.catalog_page = self.home_page.click_enter_button()
    
    def testAddingFishProductToCart(self):
        from Pages.cart_page import CartPage
        # 1. Przejdź do listy ryb
        self.catalog_page.go_to_fish_list()
        # 2. Przejdź do konkretnego gatunku ryb
        self.catalog_page.click_random_product_id()
        # 3. Dodaj do koszyka dowolną rybę
        sleep(6)
        added_item_id = self.catalog_page.add_random_item_to_cart2()
        sleep(6)
        self.cart_page = CartPage(self.driver)
        # 4. Pobierz listę produktów w koszyku
        item_ids = self.cart_page.get_all_item_ids_in_cart()
        print(item_ids) #do weryfikacji czy działa
        print(added_item_id)
        # 5. Sprawdź, czy dodany produkt znajduje się na liście produktów w koszyku
        self.assertIn(added_item_id, item_ids)