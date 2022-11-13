from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  currency = soup.find("span", class_="ccOutputRslt").get_text()
  print(currency[0: -4])






get_currency("CAD", "USD")