import requests

from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)