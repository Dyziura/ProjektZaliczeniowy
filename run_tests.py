import unittest
import HtmlTestRunner

suite = unittest.TestLoader().discover( #ładowanie testów z folderu Tests - zwraca kolekcję testów
    start_dir='Tests',
    pattern='*.py', # Filtr plików testowych - pomija pliki z innymi rozszerzeniami
)

runner = HtmlTestRunner.HTMLTestRunner(
    output='Reports', # Katalog, w którym będą zapisywane raporty
    report_name='AllTests', # Nazwa raportu
    combine_reports=True, # Łączenie raportów w jeden
    add_timestamp=True # Dodanie znacznika czasu do nazwy raportu
)

print(f"Discovered {suite.countTestCases()} test cases.")
runner.run(suite)