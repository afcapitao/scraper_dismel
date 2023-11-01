import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from common import *
import re

def main(arg):

  URL = "https://www.dismel.pt/index.php/software-livros-posteres/software-vernier"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")


  # Find all product sections
  product_sections = soup.find_all('div', class_='ba-row row-fluid ba-no-gutter rooms-row shadow3')
  softwares = []
  descs1 = []
  descs2 = []

  count=0
  for section in product_sections:
    software_span = section.find('div', class_='ba-item-text ba-item').find('p')
    software = software_span.get_text(strip=True) if software_span is not None else ''
    if software == '':
      software=software_span.find_next('p').get_text(strip=True) if software_span is not None else ''
    
    print('software: ' +software)

    desc1_div = section.find('div', class_='ba-item-text ba-item').find('div', class_='content-text')
    desc1 = desc1_div.get_text(strip=True)
    print('desc1: ' +desc1)

    desc2_div = section.find('div', class_='ba-item-accordion ba-item').find('div', class_='accordion-inner')
    desc2 = desc2_div.get_text(strip=True) if desc2_div is not None else ''
    print('desc2: ' +desc2)
   
    if software != '' and desc1 != '' and desc2 != '':
      softwares.append(software)
      descs1.append(desc1)
      descs2.append(desc2)
      count+=1

  print("total "+str(len(descs1)))

  df = pd.DataFrame({
      'produto': softwares,
      'descricao1': descs1,
      'descricao2': descs2,
  }, index=pd.RangeIndex(start=0, stop=count))

  # Save the DataFrame to an Excel file
  excel_file = 'software.xlsx'
  df.to_excel(excel_file, index=False, header=True)