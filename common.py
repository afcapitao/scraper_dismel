import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

def getURL():
  return 'https://www.dismel.pt/'

def extractDescricao(soup, isFormatted):
  divs = soup.find_all("div", class_="ba-section row-fluid shadow4")
  for section_div in divs: 
    content_text_div = section_div.find('div', class_='content-text')
    if content_text_div:
      if isFormatted == 'true':
        remove_tag(content_text_div,'div')
        remove_tag(content_text_div,'span')
        remove_tag(content_text_div,'a')
        remove_tag(content_text_div,'input')
      return content_text_div.get_text(strip=False) if isFormatted=='false' else content_text_div

def extractProductName(soup):
  row_div = soup.find('div', class_='ba-row row-fluid ba-no-gutter rooms-row')
  if row_div:
      return row_div.get_text(strip=True)

def remove_attributes(soup,attr):
  if soup is not None:
    for tag in soup.find_all(True):
        if tag.has_attr(attr):
            del tag[attr]

def filter_phrases(text):
  return text.replace("Para mais informações sobre este tópico, por favor contate a Dismel.", "")

def extractAllUrls(soup):
  divs = soup.find_all('div', class_='row-fluid container main-body ba-container-fluid')
  hrefs = []
  for div in divs:
      a_tags = div.find_all('a', class_='ba-btn-transition')
      for a_tag in a_tags:
          href = a_tag.get('href')
          if href:
              hrefs.append(href)
  return hrefs

def remove_tag(element, tagName, htmlClass=''):
  if element is not None:
    elements=element.find_all(tagName) if htmlClass=='' else element.find_all(tagName, class_=htmlClass)
    for tag in element.find_all(tagName):
      tag.unwrap()
  return element

def removeTagsNotNeeded(element):
  remove_tag(element,'div')
  remove_tag(element,'span')
  remove_tag(element,'a')
  remove_tag(element,'input')
  remove_tag(element,'img')

def buildFileName(filename, isFormatted):
  return Constants.EXTRACTION_FOLDER+filename+('' if isFormatted=='false' else Constants.FORMATTED_TEXT) + Constants.EXTENSION

class Constants:
  EXTRACTION_FOLDER="extracao/"
  FILENAME_ACESSORIOS="acessorios"
  FILENAME_EQUIP_LAB="equipamentos_laboratorio"
  FILENAME_INTERFACES="interfaces"
  FILENAME_SENS_DISP_MOV="sensores_dispositivos_moveis"
  FILENAME_SENSORES="sensores"
  FILENAME_SOFTWARE="software"
  FILENAME_KITS="kits_ciencias"
  FORMATTED_TEXT="_formatted"
  EXTENSION=".xlsx"