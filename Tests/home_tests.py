from Tests.base_test import BaseTest
from Pages.catalog_page import CatalogPage
from time import sleep

class HomeTest(BaseTest):
    
    #def setUp(self):
    #    super().setUp() #wywołanie z klasy nadrzędnej

    def testOpeningCatalogPage(self):
        # 1. Kliknij Enter the store
        self.catalog_page: CatalogPage = self.home_page.click_enter_button()
        # 2. Sprawdź, czy strona katalogu została otwarta
        self.assertTrue(self.catalog_page.is_Catalog_Page())
