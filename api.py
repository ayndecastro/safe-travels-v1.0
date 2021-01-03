import os
import flask
import json
import requests
from flask import jsonify, request
from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()

jsonFile = open('db.json')
api = json.load(jsonFile)

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/api/search/<place_id>', methods=['GET'])
def home(place_id):
    api_key = os.environ.get('GOOGLE_API_KEY')
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"

    response = requests.request("GET", url)

    return response.text


@app.route('/api/location/<location_query>', methods=['GET'])
def geo_locator(location_query):
    api_key = os.environ.get('GOOGLE_API_KEY')
    gmaps_url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={location_query}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={api_key}'
    payload = {}
    response = requests.request("GET", gmaps_url, data=payload)
    result = response.text

    return result


app.run()
