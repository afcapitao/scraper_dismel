import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from common import *

def main(isFormatted):
  print("********* Start extaction Interfaces *********")
  URL = "https://www.dismel.pt/interfaces-vernier"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")

  urls = extractAllUrls(soup)

  property_keys = ["URL", "produto", "descricao", "hardware", "software", "wireless", "acessorios", "sensorsCompatibles"]
  content = {key: [] for key in property_keys}

  for url_product in urls:
    urlProduto=URL+url_product
    print(urlProduto)
    page = requests.get(urlProduto)
    soup = BeautifulSoup(page.content, "html.parser")
    productName = extractProductName(soup,isFormatted)
    print(productName)
    #remove_attributes(soup,'style')
    #remove_tag(soup,'span')

    content["URL"].append(urlProduto)
    content["produto"].append(productName)
    content["descricao"].append(extract("tab-0", "descricao", soup, isFormatted))
    content["hardware"].append(extract("tab-1", "hardware", soup, isFormatted))
    content["software"].append(extract("tab-2", "software", soup, isFormatted))
    content["wireless"].append(extract("tab-3", "wireless", soup, isFormatted))
    content["acessorios"].append(extract("tab-4", "acessorios", soup, isFormatted))
    content["sensorsCompatibles"].append(extract("tab-5", "sensorsCompatibles", soup, isFormatted))

  df = pd.DataFrame({
      'URL': content["URL"],
      'produto': content["produto"],
      'descricao': content["descricao"],
      'hardware': content["hardware"],
      'software': content["software"],
      'wireless': content["wireless"],
      'acessorios': content["acessorios"],
      'sensorsCompatibles': content["sensorsCompatibles"]
  }, index=pd.RangeIndex(start=0, stop=len(content["produto"])))

  # Save the DataFrame to an Excel file
  excel_file = buildFileName(Constants.FILENAME_INTERFACES,isFormatted)
  df.to_excel(excel_file, index=False, header=True)
  print("********* End extaction Interfaces *********")

def extract(mainTag, groupName, soup, isFormatted):
  tab = soup.find("div", id=mainTag)
  tabStr=''
  if tab:
    tabStr=tab.extract() if isFormatted == 'true' else tab.get_text(strip=False)
    if isFormatted=='true':
      removeTagsNotNeeded(tabStr)
    tabStr=filter_phrases(tabStr)
  return tabStr

def extractProductName(soup, isFormatted):
  initialNames = soup.find_all("span", {"style":"font-size:36px;"})
  nested_span_text=''
  for initialName in initialNames:
    nested_spans = initialName.find_all("span")
    nested_span_text = nested_span_text + ' '.join([nested_span.get_text(strip=False) for nested_span in nested_spans if nested_span.get_text(strip=False)])
  if nested_span_text:
    return nested_span_text