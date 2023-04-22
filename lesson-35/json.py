import json
import googlemaps
from apikey import APIKEY


#Google maps
gmaps = googlemaps.Client(key=APIKEY)

date= gmaps.geocode('Olmazor,Tashkent,Uzbekistan')

g = json.dumps(date[0] , indent = 4 , sort_keys=True)
print(date.keys())