import requests
from pprint import pprint
# sahifa="https://kun.uz/uz/news/list"
# r=requests.get(sahifa)
# pprint(r.text)

country ="Uzbekistan"
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json =r.json()[0]

pprint(r_json["capital"])