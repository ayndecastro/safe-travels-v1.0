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


@app.route('/api/token', methods=['POST'])
def get_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    client_id = os.environ.get('AMADEUS_API_KEY'),
    client_secret = os.environ.get('AMADEUS_API_SECRET')

    payload = f'client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


@app.route('/api/search/<lat>/<lng>', methods=['GET'])
def home(lat, lng):

    url = f"https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude={lat}&longitude={lng}&radius=2"
    print(url)
    payload = {}
    headers = {
        'Authorization': 'Bearer token'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


@app.route('/api/location/<location_query>', methods=['GET'])
def geo_locator(location_query):
    api_key = os.environ.get('GOOGLE_API_KEY')
    gmaps_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location_query}&key={api_key}'
    response = requests.request("GET", gmaps_url)
    result = response.text

    return result
    # print(f"{os.environ.get(API_KEY)}")


app.run()
