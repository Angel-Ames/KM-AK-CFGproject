# Import everything that we need
# Geolocation is our other python file
import Geolocation
# Flask used to create the app
from flask import Flask, render_template, request
import requests
import os
# json and jsonify for our outputs of the API
import json
from flask.json import jsonify
# dotenv for our API keys
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# These are the API keys that are being pulled from the dotenv file.
# I gave them variables to make the code downstream a lot easier
bing_maps_key=os.getenv("API_KEY")
bing_maps_website=os.getenv("bing_maps_website")
Here_APP_ID=os.getenv("Here_APP_ID")
Here_APP_code=os.getenv("Here_APP_code")

# This is the code to create the homepage of our app
@app.route("/")
def home_page():
  return render_template("home.html")

# This is the code to create the maps. 
# note if you just enter localhost/maps you wont get anything as it needs the input text from the box
@app.route("/map", methods=["get", "post"])
def map_page():
  # This is how it gets the location from the form on the home page
  data = request.form["location"]
  # For testing and trouble shooting. To make sure its getting the information.
  print (data)
  # Naming the function from Geolocation.py
  geo = Geolocation.geolocate_input(data)
  print (geo)
  lat = geo.latitude
  lon = geo.longitude
  print(lat, lon)
  # This is the url that we need to get our information. 
  # You have to input lat and lon to get the location (make sure they are strings!)
  # Also need our API codes.
  url="https://places.cit.api.here.com/places/v1/discover/explore?in="+str(lat)+","+str(lon)+";r=2000&cat=recreation&pretty=true&size=100&app_id="+Here_APP_ID+"&app_code="+Here_APP_code
  r=requests.get(url)
  # This is to view the results in a HTML file
  # json_title = jsonify(json.loads(r.text)["results"]["items"][0]["title"])
  # result_lat = jsonify(json.loads(r.text)["results"]["items"][0]["position"][0])
  # result_lon = jsonify(json.loads(r.text)["results"]["items"][0]["position"][1])
  # This is to view it on print within the function
  json_title1 = json.loads(r.text)["results"]["items"][0]["title"]
  result_lat1 = json.loads(r.text)["results"]["items"][0]["position"][0]
  result_lon1 = json.loads(r.text)["results"]["items"][0]["position"][1]

  json_title2 = json.loads(r.text)["results"]["items"][1]["title"]
  result_lat2 = json.loads(r.text)["results"]["items"][1]["position"][0]
  result_lon2 = json.loads(r.text)["results"]["items"][1]["position"][1]

  json_title3 = json.loads(r.text)["results"]["items"][2]["title"]
  result_lat3 = json.loads(r.text)["results"]["items"][2]["position"][0]
  result_lon3 = json.loads(r.text)["results"]["items"][2]["position"][1]

  json_title4 = json.loads(r.text)["results"]["items"][3]["title"]
  result_lat4 = json.loads(r.text)["results"]["items"][3]["position"][0]
  result_lon4 = json.loads(r.text)["results"]["items"][3]["position"][1]
  
  json_title5 = json.loads(r.text)["results"]["items"][4]["title"]
  result_lat5 = json.loads(r.text)["results"]["items"][4]["position"][0]
  result_lon5 = json.loads(r.text)["results"]["items"][4]["position"][1]
  

  # render the template HTML with the values of lat and lon which are input into the map to give location
  # return render_template("map2.html", lat=lat, lon=lon, result_latitude=result_latitude, result_longitude=result_longitude, json_title=json_title)

  return render_template("map2.html", lat=lat, lon=lon, result_lat1=result_lat1, result_lon1=result_lon1, json_title1=json_title1, result_lat2=result_lat2, result_lon2=result_lon2, json_title2=json_title2, result_lat3=result_lat3, result_lon3=result_lon3, json_title3=json_title3, result_lat4=result_lat4, result_lon4=result_lon4, json_title4=json_title4, result_lat5=result_lat5, result_lon5=result_lon5, json_title5=json_title5)

# This is similar to above. This is the API HERE to get park data.
@app.route("/parks", methods=["get", "post"])
def parks_local():
  # Gave a value to sheffield just for testing
  # shef=[53.3811862411877, -1.50404644436198]
  # Getting input from input on home page
  data = request.form["park_output"]
  # print (data)
  geo = Geolocation.geolocate_input(data)
  # print (geo)
  lat = geo.latitude
  lon = geo.longitude
  # print(lat, lon)
  # This is the url that we need to get our information. 
  # You have to input lat and lon to get the location (make sure they are strings!)
  # Also need our API codes.
  url="https://places.cit.api.here.com/places/v1/discover/explore?in="+str(lat)+","+str(lon)+";r=2000&cat=recreation&pretty=true&size=100&app_id="+Here_APP_ID+"&app_code="+Here_APP_code
  # This is how we pull the data from the website above
  r=requests.get(url)
  # This makes it easier to read
  jsonr=jsonify(json.loads(r.text)["results"])
  json_title = jsonify(json.loads(r.text)["results"]["items"][0]["title"])
  result_latitude = jsonify(json.loads(r.text)["results"]["items"][0]["position"][0])
  result_longitude = jsonify(json.loads(r.text)["results"]["items"][0]["position"][1])

  
  
  print(result_list)


# This is for the about page
@app.route("/about")
def about_page():
  return render_template("about.html")

@app.route("/GreenSpace")
def GreenSpace_page():
  return render_template("GreenSpace.html")

@app.route("/Contact")
def Contact_page():
  return render_template("Contact.html")


if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)