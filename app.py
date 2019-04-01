# Import flask
import Geolocation
from flask import Flask, render_template, request
import requests
import os
import json
from flask.json import jsonify

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

bing_maps_website=os.getenv("bing_maps_website")
Here_APP_ID=os.getenv("Here_APP_ID")
Here_APP_code=os.getenv("Here_APP_code")

@app.route("/")
def home_page():
  return render_template("home.html")

@app.route("/maps", methods=["post"])
def map_page():
  data = request.form["location"]
  print (data)
  geo = Geolocation.geolocate_input(data)
  print (geo)
  lat = geo.latitude
  lon = geo.longitude
  print(lat, lon)
  return render_template("map.html", lat=lat, lon=lon)

@app.route("/parks", methods=["get", "post"])
def parks_local():
  shef=[53.3811862411877, -1.50404644436198]
  data = request.form["park_output"]
  print (data)
  geo = Geolocation.geolocate_input(data)
  print (geo)
  lat = geo.latitude
  lon = geo.longitude
  print(lat, lon)
  url="https://places.cit.api.here.com/places/v1/discover/explore?in="+str(lat)+","+str(lon)+";r=2000&cat=recreation&pretty=true&size=100&app_id="+Here_APP_ID+"&app_code="+Here_APP_code
  r=requests.get(url)
  return jsonify(json.loads(r.text)["results"])



@app.route("/about")
def about_page():
  return render_template("about.html")

app.run(debug=True)