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

---

## Struktura projektu

<pre> Projekt/ ├── Pages/ # Page Object classes ├── Tests/ # Test cases (unittest) ├── Test_data/ # Pliki CSV / dane testowe ├── venv/ # Środowisko wirtualne (nie commituj) ├── requirements.txt # Lista zależności └── README.md # Ten plik </pre>

---

## Uruchamianie testów

- python -m unittest discover -s Tests -p '*_tests.py'

## Od autora

- Projekt testowy stworzony do celów edukacyjnych i praktyki automatyzacji E2E.