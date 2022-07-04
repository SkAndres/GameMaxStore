from django.test import TestCase
import googlemaps
from datetime import datetime


import requests

url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Paris&types=geocode&key=AIzaSyDEWvBrnVegE07kwLYp-wHr2DT-1N19nd4"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)