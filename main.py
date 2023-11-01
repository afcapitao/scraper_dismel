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

def main():
  scraper=sys.argv[1]
  withFormat=sys.argv[2]
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


if __name__ == "__main__":
    main()