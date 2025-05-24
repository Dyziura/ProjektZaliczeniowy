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
    
    def test_TC_00007_SearchingInaccessibleProducts(self):
        """TC_00007: Wyszukiwanie produktów, które nie istnieją w katalogu"""
        print("TC_00007: Wyszukiwanie produktów, które nie istnieją w katalogu")
        from Pages.catalog_page import CatalogPageVariables
        # 1. Wpisz coś do pola search
        # 2. Kliknij Search
        self.catalog_page.enter_search_value("")
        # Sprawdź, czy pojawił się alert: "Please enter a keyword to search for, then press the search button."
        self.assertEqual(CatalogPageVariables.infoMessageSearchField, self.catalog_page.get_alert_message())
        #self.assertEqual("Please enter a keyword to search for, then press the search button.", self.catalog_page.get_alert_message())

    def test_TC_00008_SearchingAccessibleRandomProduct(self):
        """TC_00008: Wyszukiwanie losowego produktu, pobranego z pliku CSV - dokumentacja wszystkich produktów"""
        print("TC_00008: Wyszukiwanie losowego produktu, pobranego z pliku CSV - dokumentacja wszystkich produktów")
        row = random.choice(self.test_data)

        description = row['Description']
        expected_short_description = row['ShortDescription']
        # 1. Wpisz coś do pola search
        # 2. Kliknij Search
        self.catalog_page.enter_search_value(description)
        # Sprawdź, czy treść wyszukiwana została znaleziona"
        self.assertEqual(expected_short_description, self.catalog_page.get_name_product())

    def test_TC_00009_ClickingSignInButton(self):
        """TC_00009: Przejście do strony logowania ze strony z produktami poprzez kliknięcie Sign In"""
        print("TC_00009: Przejście do strony logowania ze strony z produktami poprzez kliknięcie Sign In")
        from Pages.sign_in_page import SignInPageVariables
        # 1. Kliknij Sign In
        self.catalog_page.sign_in_button()
                # 1. Kliknij Cart
        # 2. Sprawdź, czy strona koszyka została otwarta
        self.sign_in_page = self.catalog_page.sign_in_button()
        self.assertEqual(SignInPageVariables.signInPageText, self.sign_in_page.is_Sign_In_Page())

    def test_TC_00010_GoingToCatsList(self):
        """TC_00010: Przejście do strony wyboru rozmiaru/gatunku kota ze strony z produktami poprzez kliknięcie portretu kota"""
        print("TC_00010: Przejście do strony wyboru rozmiaru/gatunku kota ze strony z produktami poprzez kliknięcie portretu kota")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy kotów - portret
        # 2. Przejdź do listy kotów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.catsList)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleCatsList, title)

    def test_TC_00011_GoingToFishList(self):
        """TC_00011: Przejście do strony wyboru rozmiaru/gatunku ryby ze strony z produktami poprzez kliknięcie portretu ryby"""
        print("TC_00011: Przejście do strony wyboru rozmiaru/gatunku ryby ze strony z produktami poprzez kliknięcie portretu ryby")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy ryb - portret
        # 2. Przejdź do listy ryb
        self.catalog_page.go_to_animal_list(CatalogPageLocators.fishList)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleFishList, title)

    def test_TC_00012_GoingToDogsList(self):
        """TC_00012: Przejście do strony wyboru rozmiaru/gatunku psa ze strony z produktami poprzez kliknięcie portretu psa"""
        print("TC_00012: Przejście do strony wyboru rozmiaru/gatunku psa ze strony z produktami poprzez kliknięcie portretu psa")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy psów - portret
        # 2. Przejdź do listy psów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.dogsList)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleDogsList, title)

    def test_TC_00013_GoingToReptilesList(self):
        """TC_00013: Przejście do strony wyboru rozmiaru/gatunku gada ze strony z produktami poprzez kliknięcie portretu gada"""
        print("TC_00013: Przejście do strony wyboru rozmiaru/gatunku gada ze strony z produktami poprzez kliknięcie portretu gada")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy gadów - portret
        # 2. Przejdź do listy gadów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.reptilesList)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleReptilesList, title)

    def test_TC_00014_GoingToBirdsList(self):
        """TC_00014: Przejście do strony wyboru rozmiaru/gatunku ptaka ze strony z produktami poprzez kliknięcie portretu ptaka"""
        print("TC_00014: Przejście do strony wyboru rozmiaru/gatunku ptaka ze strony z produktami poprzez kliknięcie portretu ptaka")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy ptaków - portret
        # 2. Przejdź do listy ptaków
        self.catalog_page.go_to_animal_list(CatalogPageLocators.birdsList)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleBirdsList, title)
    
    def test_TC_00015_GoingToCatsList2(self):
        """TC_00015: Przejście do strony wyboru rozmiaru/gatunku kota ze strony z produktami poprzez kliknięcie napisu Cats pod koszykiem"""
        print("TC_00015: Przejście do strony wyboru rozmiaru/gatunku kota ze strony z produktami poprzez kliknięcie napisu Cats pod koszykiem")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy kotów - napis pod koszykiem
        # 2. Przejdź do listy kotów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.catsList2)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleCatsList, title)
    
    def test_TC_00016_GoingToFishList2(self):
        """TC_00016: Przejście do strony wyboru rozmiaru/gatunku ryby ze strony z produktami poprzez kliknięcie napisu Fish pod koszykiem"""
        print("TC_00016: Przejście do strony wyboru rozmiaru/gatunku ryby ze strony z produktami poprzez kliknięcie napisu Fish pod koszykiem")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy ryb - napis pod koszykiem
        # 2. Przejdź do listy ryb
        self.catalog_page.go_to_animal_list(CatalogPageLocators.fishList2)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleFishList, title)

    def test_TC_00017_GoingToDogsList2(self):
        """TC_00017: Przejście do strony wyboru rozmiaru/gatunku psa ze strony z produktami poprzez kliknięcie napisu Dogs pod koszykiem"""
        print("TC_00017: Przejście do strony wyboru rozmiaru/gatunku psa ze strony z produktami poprzez kliknięcie napisu Dogs pod koszykiem")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy psów - napis pod koszykiem
        # 2. Przejdź do listy psów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.dogsList2)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleDogsList, title)

    def test_TC_00018_GoingToReptilesList2(self):
        """TC_00018: Przejście do strony wyboru rozmiaru/gatunku gada ze strony z produktami poprzez kliknięcie napisu Reptiles pod koszykiem"""
        print("TC_00018: Przejście do strony wyboru rozmiaru/gatunku gada ze strony z produktami poprzez kliknięcie napisu Reptiles pod koszykiem")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy gadów - napis pod koszykiem
        # 2. Przejdź do listy gadów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.reptilesList2)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleReptilesList, title)

    def test_TC_00019_GoingToBirdsList2(self):
        """TC_00019: Przejście do strony wyboru rozmiaru/gatunku ptaka ze strony z produktami poprzez kliknięcie napisu Birds pod koszykiem"""
        print("TC_00019: Przejście do strony wyboru rozmiaru/gatunku ptaka ze strony z produktami poprzez kliknięcie napisu Birds pod koszykiem")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy ptaków - napis pod koszykiem
        # 2. Przejdź do listy ptaków
        self.catalog_page.go_to_animal_list(CatalogPageLocators.birdsList2)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleBirdsList, title)
    
    def test_TC_00020_GoingToCatsList3(self):
        """TC_00020: Przejście do strony wyboru rozmiaru/gatunku kota ze strony z produktami poprzez kliknięcie napisu Cats z rodzajami do listy kotów"""
        print("TC_00020: Przejście do strony wyboru rozmiaru/gatunku kota ze strony z produktami poprzez kliknięcie napisu z rodzajami do listy kotów")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy kotów - napis z rodzajami do listy kotów
        # 2. Przejdź do listy kotów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.catsList3)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleCatsList, title)

    def test_TC_00021_GoingToFishList3(self):
        """TC_00021: Przejście do strony wyboru rozmiaru/gatunku ryby ze strony z produktami poprzez kliknięcie napisu Fish z rodzajami do listy ryb"""
        print("TC_00021: Przejście do strony wyboru rozmiaru/gatunku ryby ze strony z produktami poprzez kliknięcie napisu z rodzajami do listy ryb")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy ryb - napis z rodzajami do listy ryb
        # 2. Przejdź do listy ryb
        self.catalog_page.go_to_animal_list(CatalogPageLocators.fishList3)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleFishList, title)

    def test_TC_00022_GoingToDogsList3(self):
        """TC_00022: Przejście do strony wyboru rozmiaru/gatunku psa ze strony z produktami poprzez kliknięcie napisu Dogs z rodzajami do listy psów"""
        print("TC_00022: Przejście do strony wyboru rozmiaru/gatunku psa ze strony z produktami poprzez kliknięcie napisu z rodzajami do listy psów")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy psów - napis z rodzajami do listy psów
        # 2. Przejdź do listy psów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.dogsList3)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleDogsList, title)

    def test_TC_00023_GoingToReptilesList3(self):
        """TC_00023: Przejście do strony wyboru rozmiaru/gatunku gada ze strony z produktami poprzez kliknięcie napisu Reptiles z rodzajami do listy gadów"""
        print("TC_00023: Przejście do strony wyboru rozmiaru/gatunku gada ze strony z produktami poprzez kliknięcie napisu Repitles z rodzajami do listy gadów")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy gadów - napis z rodzajami do listy gadów
        # 2. Przejdź do listy gadów
        self.catalog_page.go_to_animal_list(CatalogPageLocators.reptilesList3)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleReptilesList, title)
    
    def test_TC_00024_GoingToBirdsList3(self):
        """TC_00024: Przejście do strony wyboru rozmiaru/gatunku ptaka ze strony z produktami poprzez kliknięcie napisu Birds z rodzajami do listy ptaków"""
        print("TC_00024: Przejście do strony wyboru rozmiaru/gatunku ptaka ze strony z produktami poprzez kliknięcie napisu Birds z rodzajami do listy ptaków")
        from Pages.catalog_page import CatalogPageLocators, CatalogPageVariables
        # 1. Kliknij link do listy ptaków - napis z rodzajami do listy ptaków
        # 2. Przejdź do listy ptaków
        self.catalog_page.go_to_animal_list(CatalogPageLocators.birdsList3)
        # 2. Sprawdź, czy strona listy zwierząt została otwarta - weryfikacja tytułu
        title = self.catalog_page.get_title_animal_list()
        self.assertEqual(CatalogPageVariables.titleBirdsList, title)

    def test_TC_00025_GoingToCartPage(self):
        """TC_00025: Przejście do strony koszyka ze strony z produktami poprzez kliknięcie Cart"""
        print("TC_00025: Przejście do strony koszyka ze strony z produktami poprzez kliknięcie Cart")
        # 1. Kliknij Cart
        # 2. Sprawdź, czy strona koszyka została otwarta
        self.cart_page = self.catalog_page.cart_button()
        self.assertTrue(self.cart_page.is_Cart_Page())
    
    def test_TC_00026_IsItCatalogPage(self):
        """TC_00026: Sprawdzenie, czy strona katalogu została otwarta"""
        print("TC_00026: Sprawdzenie, czy strona katalogu została otwarta")
        # 1. Sprawdź, czy strona katalogu została otwarta
        self.assertTrue(self.catalog_page.is_Catalog_Page())

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