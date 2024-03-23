from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def initialize_driver():
  # chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

  chrome_options = Options()
  options = [
      "--headless",
      "--disable-gpu",
      "--window-size=1920,1200",
      "--ignore-certificate-errors",
      "--disable-extensions",
      "--no-sandbox",
      "--disable-dev-shm-usage"
  ]
  for option in options:
      chrome_options.add_argument(option)

  driver = webdriver.Chrome(options=chrome_options)

  return driver

def get_html_content(driver, URL: str):
  driver.get(URL)
  page = driver.page_source
  soup = BeautifulSoup(page, features="html.parser")

  return soup

def get_content_from_container(soup: BeautifulSoup, container: str):
  return soup.find_all(container)


