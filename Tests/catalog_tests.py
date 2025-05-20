from Tests.base_test import BaseTest
from time import sleep
from Test_data.csv_reader import get_test_data
import random

class CatalogTest(BaseTest):
    
    @classmethod
    def setUpClass(cls):
        #super().setUpClass() - aktualnie niepotrzebne ponieważ w klasie nadrzędnej nie ma metody setUpClass unittest.TestCase ma domyślną (pustą) implementację setUpClass(), więc nie kończyło się błędem
        # 1. Wczytaj dane testowe z pliku CSV
        cls.test_data = get_test_data('Test_data/products.csv') #tearDownClass() nie jest potrzebne, jeśli tylko wczytujesz dane z CSV.

    def setUp(self):
        super().setUp() #wywołanie z klasy nadrzędnej z base_test.py
        # 1. Załadowanie strony catalogu
        self.catalog_page = self.home_page.click_enter_button()
    
    def testSearchingInaccessibleProducts(self):
        # 1. Wpisz coś do pola search
        sleep(2)
        # 2. Kliknij Search
        self.catalog_page.enter_search_value("")
        sleep(2)
        # Sprawdź, czy pojawił się alert: "Please enter a keyword to search for, then press the search button."
        self.assertEqual("Please enter a keyword to search for, then press the search button.", self.catalog_page.get_alert_message())
        sleep(2)

    def testSearchingAccessibleRandomProduct(self):
        row = random.choice(self.test_data)

        description = row['Description']
        expected_short_description = row['ShortDescription']
        # 1. Wpisz coś do pola search
        sleep(2)
        # 2. Kliknij Search
        self.catalog_page.enter_search_value(description)
        sleep(2)
        # Sprawdź, czy treść wyszukiwana została znaleziona"
        self.assertEqual(expected_short_description, self.catalog_page.get_name_product())
        sleep(2)

    def testClickingSignInButton(self):
        # 1. Kliknij Sign In
        self.catalog_page.sign_in_button()
        sleep(2)
        # 2. Sprawdź, czy strona logowania została otwarta
        #self.assertTrue(self.catalog_page.is_Sign_In_Page())
        #sleep(2)

""" musze dopracowac aby po kazdym tescie klikalo w search i czyscilo pole search szykujac pole pod nowe dane
    def testSearchingAccessibleAllProducts(self):
        for row in self.test_data: #wykona wszystkie testy par z pliku CSV
            description = row['Description']
            expected_short_description = row['ShortDescription']
            
            with self.subTest(description=description): #każdy przypadek będzie raportowany oddzielnie w wynikach testów
                # 1. Wpisz coś do pola search
                sleep(2)
                # 2. Kliknij Search
                self.catalog_page.enter_search_value(description)
                sleep(2)
                # Sprawdź, czy pojawił się alert: "Please enter a keyword to search for, then press the search button."
                self.assertEqual(expected_short_description, self.catalog_page.get_name_product())
                sleep(2)
"""    