# This is a python file that gets the lat and long values from a place.
import json
import sys
import ssl
import certifi
import geopy.geocoders
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
from geopy.geocoders import Nominatim
import geopy
from dotenv import load_dotenv
load_dotenv()
import json
from flask.json import jsonify	

# def geolocate_input(json_file):
#     geolocator = Nominatim()
#     short_json = json_file
#     result = []
    
#     try:
#         location = geolocator.geocode(json_file, timeout = 1)
#         if location != None:
#             item['address'] = location.address
#             item['lng'] = location.longitude
#             item['lat'] = location.latitude
#             result.append(item)
#             continue
#     except geopy.exc.GeocoderTimedOut:
#         pass		
#     return result

def geolocate_input(json_file):
    geolocator = Nominatim()
# This gets the geocode and times it out if it gets to long
    location = geolocator.geocode(json_file, timeout = 1)
    return location



