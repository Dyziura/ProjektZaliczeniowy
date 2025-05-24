import unittest
import HtmlTestRunner

# Import klas testowych
from Tests.sign_in_tests import SignInTest
from Tests.catalog_tests import CatalogTest
from Tests.cart_tests import CartTest

# Tworzenie TestSuite i dodawanie wybranych testów
suite = unittest.TestSuite()

suite.addTest(CatalogTest('test_TC_00007_SearchingInaccessibleProducts'))
suite.addTest(CatalogTest('test_TC_00008_SearchingAccessibleRandomProduct'))
#suite.addTest(SignInTest('testLogInInvalid'))
#suite.addTest(CatalogTest('testSearchingInaccessibleProducts'))
#suite.addTest(CatalogTest('testSearchingAccessibleRandomProduct'))

# Konfiguracja HtmlTestRunner - szczegółowy opis konfiguracji w run_tests.py
runner = HtmlTestRunner.HTMLTestRunner(
    output='Reports',
    report_name='SelectedTests',
    combine_reports=True,
    add_timestamp=True
)

print(f"Discovered {suite.countTestCases()} selected test cases.")
runner.run(suite)