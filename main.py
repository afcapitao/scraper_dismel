import requests
import csv
import pandas as pd
import sys
from bs4 import BeautifulSoup
from interfaces import main as interfaces
from equipamentos_laboratorio import main as equipamentos_laboratorio
from sensores import main as sensores
from sensores_dispositivos_moveis import main as sensores_dispositivos_moveis
from software import main as software
from acessorios import main as acessorios
from kits_ciencias import main as kits_ciencias

def main():
  scraper=''
  withFormat=''
  try:
    scraper=sys.argv[1]
    withFormat=sys.argv[2]
  except Exception as e:
    print("***Correr comando: python main.py <nome_do_scraper> <com_formatacao>")
    print("***Exemplo: python main.py sensores true")

  if scraper=='interfaces':
    interfaces(withFormat)
  elif scraper=='equipamentos_laboratorio':
    equipamentos_laboratorio(withFormat)
  elif scraper=='sensores':
    sensores(withFormat)
  elif scraper=='sensores_dispositivos_moveis':
    sensores_dispositivos_moveis(withFormat)
  elif scraper=='software':
    software(withFormat)
  elif scraper=='acessorios':
    acessorios(withFormat)
  elif scraper=='kits_ciencias':
    kits_ciencias(withFormat)
  elif scraper=='all':
    acessorios(withFormat)  
    interfaces(withFormat)
    equipamentos_laboratorio(withFormat)
    sensores(withFormat)
    sensores_dispositivos_moveis(withFormat)
    software(withFormat)  
    kits_ciencias(withFormat)        

if __name__ == "__main__":
    main()