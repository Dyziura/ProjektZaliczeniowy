from Tests.base_test import BaseTest
from time import sleep

class SignInTest(BaseTest):
    
    def setUp(self):
        super().setUp() #wywołanie z klasy nadrzędnej z base_test.py
        # 1. Załadowanie strony catalogu
        self.catalog_page = self.home_page.click_enter_button()
        # 2. Załadowanie strony logowania
        self.sign_in_page = self.catalog_page.sign_in_button()

    def test_TC_00028_LogInInvalid(self):
        """TC_00028: Logowanie z użyciem nieprawidłowych danych logowania"""
        print("TC_00028: Logowanie z użyciem nieprawidłowych danych logowania")
        from Pages.sign_in_page import SignInPageVariables
        from Test_data.data_generator import FakeData
        fake = FakeData()

        username = fake.get_username()
        password = fake.get_password()
        # 1. Wprowadź dane z Fakera do pola username
        self.sign_in_page.type_in_username(username)
        # 2. Wprowadź dane z Fakera do pola password
        self.sign_in_page.type_in_password(password)
        # 3. Kliknij Login
        self.sign_in_page.click_login_button()
        # 4. Sprawdź, czy pojawił się alert: "Invalid username or password.  Signon failed."
        self.assertEqual(SignInPageVariables.invalidUsernamePassword, self.sign_in_page.get_alert_message())
