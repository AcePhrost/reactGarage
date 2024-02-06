from flask import Flask,request
from uuid import uuid4


from app import app
from db import card, users

@app.get('/card')
def get_cards():
  return { 'card': list(card.values()) }

@app.get('/card/<card_id>')
def get_card(card_id):
    try:
        return {'card': card[card_id]}, 200
    except KeyError:
        return {'message': "Invalid card"}, 400

@app.post('/card/<card_id>')
def add_card(card_id):
  card_data = request.get_json()
  user_id = card_data['user_id']
  if user_id in users:
    card[uuid4()] = card_data
    return { 'message': "Card Added" }, 201
  return { 'message': "Returned Card"}, 401

@app.put('/card/<card_id>')
def upgrade_card(card_id):
    try:
        c = card[card_id]
        card_data = request.get_json()
        if card_data['user_id'] == c['user_id']:
            c['model'] = card_data['model']
            return { 'message': 'Card Upgraded' }, 202
        # return {'message': "Upgrade Unsuccessful"}, 401
    except Exception as ex:
        print(ex)
        return {'message': "Not enough tokens"}, 400

@app.delete('/card/<card_id>')
def remove_card(card_id):
  try:
    del card[card_id]
    return {"message": "Card Deleted"}, 202
  except:
    return {'message':"Invalid Card"}, 400