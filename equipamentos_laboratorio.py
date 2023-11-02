import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from common import *

def main(isFormatted):
  print("********* Start extaction Equipamentos Laboratório *********")
  URL = "https://www.dismel.pt/equipamento-laboratorio-vernier"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")

  urls = extractAllUrls(soup)
  urls = [href for href in urls if href != "/index.php?option=com_bagrid&view=page&id=397" and href != "#"]

  property_keys = ["URL", "produto", "descricao", "especificacoes", "acessorios", "items_incluidos", "compatibilidades"]
  content = {key: [] for key in property_keys}
 
  count = 0
  for url_product in urls:
    urlProduto=URL+url_product
    print(urlProduto)
    page = requests.get(urlProduto)
    soup = BeautifulSoup(page.content, "html.parser")
    productName = extractProductName(soup)
    print(productName)

    accordion_sections = soup.find_all('div', class_='accordion-group')
    remove_attributes(soup,'style')
    
    i = 1
    content["URL"].append(urlProduto)
    content["produto"].append(productName)
    content["descricao"].append(extractDescricao(soup, isFormatted))
    for section in accordion_sections:
      accordion_heading_text = section.find('div', class_='accordion-heading')
      accordion_inner_text = section.find('div', class_='accordion-inner')

      header = accordion_heading_text.get_text(strip=True)
      text = accordion_inner_text.get_text(strip=True) if isFormatted == 'false' else accordion_inner_text.extract()

      if isFormatted=='true':
          removeTagsNotNeeded(text)

      if header.find('specificações') != -1:
        content['especificacoes'].append(text)
      elif header.find('cessórios') != -1:
        content['acessorios'].append(text)
      elif header.find('tens Incluidos') != -1:
        content['items_incluidos'].append(text)
      elif header.find('ompatibilidades') != -1:
        content['compatibilidades'].append(text)
    
    count+=1

    #add empty value
    for key in property_keys:
      print(key + ' count: ' + str(len(content[key])))
      if len(content[key]) < count:
        content[key].append('')

  for key, value in content.items():
    print(f"{key}: {len(value)}")

  df = pd.DataFrame({
      'url': content["URL"],
      'produto': content["produto"],
      'descricao': content["descricao"],
      'especificacoes': content["especificacoes"],
      'acessorios': content["acessorios"],
      'items_incluidos': content["items_incluidos"],
      'compatibilidades': content["compatibilidades"]
  }, index=pd.RangeIndex(start=0, stop=count))

  # Save the DataFrame to an Excel file

  excel_file = buildFileName(Constants.FILENAME_EQUIP_LAB,isFormatted)  
  df.to_excel(excel_file, index=False, header=True)
  print("********* End extaction Equipamentos Laboratório *********")