from flask import Flask
from flask_cors import CORS
from db import card
app = Flask(__name__)
import requests


headers= {'accept': 'application/json'}
r = requests.post('https://carapi.app/api/auth/login', headers=headers, json={
  "api_token": "aded5760-eeca-47b3-b53b-921a515f645d",
  "api_secret": "138e809e2b0cf8a41bea33ab9f450d59"
})
token = r.text
headers['Authorization'] = 'Bearer ' + token
r = requests.get('https://carapi.app/api/models', headers=headers, params={'verbose': 'yes', 'year': '2019'})
data = r.json()
id = 1
for item in data['data']:
    card[str(id)] = {
        'year': '2019',
        'make': item['make']['name'],
        'model': item['name']
    }
    # data.make.name
    id += 1
CORS(app)

from resources.card import routes
from resources.user import routes