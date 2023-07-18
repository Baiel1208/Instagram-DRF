import requests
from bs4 import BeautifulSoup



url = "https://blablacar.ru/"  
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, features="html.parser")

print(soup)