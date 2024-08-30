import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.codewithharry.com/")

soup = BeautifulSoup(req.content,"html.parser")

res = soup.title


print(res.prettify{})