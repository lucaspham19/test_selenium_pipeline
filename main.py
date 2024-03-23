print("Hello GH Action")
import requests
from bs4 import BeautifulSoup

def get_html_content(URL: str):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')

  return soup

def get_content(soup: BeautifulSoup, container: str):
  return soup.find_all(container)


