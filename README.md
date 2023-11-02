# scraper_dismel

This projects is a scraper of Vernier products from dismel store.

Installation:
1) Download and Install python (https://www.python.org/downloads/)

2) Create venv (https://realpython.com/python-virtual-environments-a-primer/)

3) install libs:
    pip install requests
    pip install pandas
    pip install bs4
    pip install openpyxl

Running scraper:

- In command line: python main.py <scraper_name> <with_format>

- Example: python main.py acessorios true

- Extracion will be stored in excel file in folder "extracao".