import flask
import json
import requests
from flask import jsonify, request

jsonFile = open('db.json')
api = json.load(jsonFile)

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# imdb api link
url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/game_of_"

queryString = 'game of thr'

headers = {
    'x-rapidapi-key': "639a19526cmsh25c87cdd24fceafp19c5bbjsnddff03716412",
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
}

# search movies


@app.route('/api/search', methods=['GET'])
def home():
    response = requests.request(
        "GET", url, headers=headers, params=queryString)
    return response.text


app.run()
