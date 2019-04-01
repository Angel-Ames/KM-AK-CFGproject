import json
import sys
import ssl
import certifi
import geopy.geocoders
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
from geopy.geocoders import Nominatim
import geopy
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

    location = geolocator.geocode(json_file, timeout = 1)
    return location


