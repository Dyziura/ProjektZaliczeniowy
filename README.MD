# JPetStore Test Automation

Testy automatyczne aplikacji [JPetStore](https://petstore.octoperf.com) z użyciem:
- Python `unittest`
- Selenium WebDriver
- Page Object Pattern

---

## Wymagania

- Python `>=3.10`
- Google Chrome (lub inna przeglądarka)
- Środowisko wirtualne (rekomendowane)
- Biblioteki do pobrania w pliku requirements.txt

---

## Struktura projektu

<pre> 
Projekt/ 
├── Pages/ # Page Object classes 
├── Tests/ # Test cases (unittest) 
├── Test_data/ # Pliki CSV / dane testowe 
├── venv/ # Środowisko wirtualne (nie commituj) 
├── requirements.txt # Lista zależności 
└── README.md # Ten plik </pre>

---

## Uruchamianie testów

Wszystkich testów z poziomu Projektu wraz z generowaniem raportu:

- python run_test.py

Pojedynczych testów z poziomu Projektu (w pliku należy wprowadzić nazwy testów, które chcemy puścić) wraz z generowaniem raportu:

- python run_selected_tests.py

UWAGA: W plikach z testami dekoratorem można oznaczyć testy do pominięcia w programach run_test.py oraz run_selected_tests.py. Przykład: @unittest.skip("Tymczasowo wylaczony test. Wymaga dopracowania").

## Od autora

- Projekt testowy stworzony do celów edukacyjnych i praktyki automatyzacji E2E.