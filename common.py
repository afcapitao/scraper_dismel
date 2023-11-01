import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

def getURL():
  return 'https://www.dismel.pt/'

def extractDescricao(soup):
  divs = soup.find_all("div", class_="ba-section row-fluid shadow4")
  for section_div in divs: 
    content_text_div = section_div.find('div', class_='content-text')
    if content_text_div:
        return content_text_div.get_text(strip=True)

def extractProductName(soup):
  row_div = soup.find('div', class_='ba-row row-fluid ba-no-gutter rooms-row')
  if row_div:
      text = row_div.get_text(strip=True)
      return text

def remove_style_attributes(soup):
    for tag in soup.find_all(True):
        if tag.has_attr("style"):
            del tag["style"]

def filter_phrases(tabStr):
  tabStr=tabStr.replace("\n","")
  return tabStr.replace("<p><em>Para mais informações sobre este tópico, por favor contate a Dismel. </em></p>", "")

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

if __name__ == "__main__":
    main()