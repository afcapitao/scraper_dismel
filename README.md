# Scraper Dismel

This projects is a scraper of Vernier products from dismel store (https://www.dismel.pt/)

Installation:
1) Download and Install python (https://www.python.org/downloads/)

2) Create venv (https://realpython.com/python-virtual-environments-a-primer/)

3) install libs:
    - pip install requests
    - pip install pandas
    - pip install bs4
    - pip install openpyxl

Running scraper:

- In command line: python main.py <scraper_name> <with_format>
    - with_format=true -> this will keep html tags such as p, ul, li, strong, em
    - scraper_names -> acessorios | interfaces | equipamentos_laboratorio | kits_ciencias | sensores | sensores_dispositivos_moveis | software
- Examples:
    - python main.py acessorios true
    - python main.py all true
- Extracion will be stored in excel file in folder "extracao"
