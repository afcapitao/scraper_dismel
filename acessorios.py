import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from common import *
import re

def main(arg):
  URL = "https://www.dismel.pt/index.php/equipamento-laboratorio/vernier/acessorios"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")

  # Find all product sections
  product_sections = soup.find_all('div', class_='span8 ba-grid-column ui-sortable item-entry') + soup.find_all('div', class_='span7 ba-grid-column ui-sortable item-entry')

  product_names = []
  descriptions = []

  count=0
  for section in product_sections:
    product_name_span = section.find('span', style=re.compile(r'font-size:\s*16px', re.I))
    product_name = ''
    if arg == 'false':
      product_name = product_name_span.get_text(strip=True) if product_name_span is not None else ''
    else:
      product_name = product_name_span if product_name_span is not None else ''

    description_span = section.find('span', style=re.compile(r'font-size:\s*14px', re.I))
    description = ''
    if arg == 'false':
      description = description_span.get_text(strip=True) if description_span is not None else ''
    else:
      description = description_span if description_span is not None else ''
    if description != '' and product_name != '' and product_name not in getExcludedProducts():
      descriptions.append(description)
      product_names.append(product_name)
      count+=1


  print("total "+str(len(descriptions)))

  df = pd.DataFrame({
      'produto': product_names,
      'descricao': descriptions,
  }, index=pd.RangeIndex(start=0, stop=count))

  # Save the DataFrame to an Excel file
  if arg=='false':
    excel_file = 'acessorios.xlsx'
  else:
    excel_file = 'acessorios_formatted.xlsx'
  df.to_excel(excel_file, index=False, header=True)

def getExcludedProducts():
  return ['Termómetros de álcool','Gerador de sinais audio  (Refª 2290.50)','Fonte de tensão regulável (baixas tensões)  (Refª 2407.75)','Suportes para laboratório e acessórios','Condutores e contactos eléctricos (Refª 2522.02-14)']