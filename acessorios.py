import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from common import *
import re

def main(isFormatted):
  print("********* Start extaction Acessorios *********")
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
    product_name = product_name_span.get_text(strip=True) if product_name_span is not None else ''
    print(product_name)

    description_span = section.find('span', style=re.compile(r'font-size:\s*14px', re.I))
    description = ''

    remove_tag(description_span, 'span')
    remove_attributes(description_span, 'style')

    if isFormatted == 'false':
      description = description_span.get_text(strip=True) if description_span is not None else ''
    else:
      description = description_span.parent.extract() if description_span is not None else ''

    if product_name != '':
      toExclude=False
      for pToExclude in getExcludedProducts():
        if str(product_name).count(pToExclude)>0:
          toExclude=True
          break
      if toExclude==False:
        if isFormatted == 'true':
          removeTagsNotNeeded(description)
        descriptions.append(description)
        product_names.append(product_name)
        count+=1


  print("total "+str(len(descriptions)))

  df = pd.DataFrame({
      'produto': product_names,
      'descricao': descriptions,
  }, index=pd.RangeIndex(start=0, stop=count))

  # Save the DataFrame to an Excel file
  excel_file = buildFileName(Constants.FILENAME_ACESSORIOS,isFormatted)
  df.to_excel(excel_file, index=False, header=True)
  print("********* End extaction Acessorios *********")

def getExcludedProducts():
  return ['Termómetros de álcool','Gerador de sinais audio  (Refª 2290.50)','Fonte de tensão regulável (baixas tensões)  (Refª 2407.75)','Suportes para laboratório e acessórios','Condutores e contactos eléctricos (Refª 2522.02-14)']