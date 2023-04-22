import requests
from bs4 import  BeautifulSoup
from pprint import pprint

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
pprint(r.text)

soup = BeautifulSoup(r.text , 'html.parser')

news = soup.find_all(clas ='news-title')
pprint(news[0].text)