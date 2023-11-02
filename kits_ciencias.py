import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from common import *
import re

def main(isFormatted):
  print("********* Start extaction Kits Ciências *********")
  URL = "https://www.dismel.pt/index.php/kits-ciencias/vernier"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")


  # Find all product sections
  product_sections = soup.find_all('div', class_='ba-wrapper ba-container')[1:]
  #container_items = container[1:]
  #product_sections=container_items.find_all('div', class_="ba-row row-fluid shadow3")
  kits = []
  descs = []

  count=0
  for section_prod in product_sections:
    sections=section_prod.find_all('div', class_="ba-row row-fluid shadow3")
    for section in sections:

      kit=section.find_all('div', class_="span6 ba-grid-column ui-sortable item-entry")

      if kit != []:
        produto=kit[0].get_text(strip=True)
        kits.append(produto)

        descricao=kit[1] if isFormatted=='true' else kit[1].get_text(strip=False)
        if isFormatted=='true':
          removeTagsNotNeeded(descricao)
          descricao.extract()

        descs.append(descricao)
        count+=1

  print("total "+str(len(descs)))

  df = pd.DataFrame({
      'produto': kits,
      'descricao1': descs
  }, index=pd.RangeIndex(start=0, stop=count))

  # Save the DataFrame to an Excel file
  excel_file = buildFileName(Constants.FILENAME_KITS,isFormatted)
  df.to_excel(excel_file, index=False, header=True)
  print("********* End extaction Kits Ciências *********")
