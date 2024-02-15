from flask import Flask, request, jsonify
from uuid import uuid4
from db import card, users  # Assuming you have imported your data structures correctly
from app import app
from models.card_model import CardModel
from models.users_model import UserModel
@app.route('/api/card', methods=['GET'])
def get_cards():
    return { 'card': list(card.values()) }

@app.route('/api/card/user/<user_id>', methods=['GET'])
def get_user_card(user_id):
    card=CardModel()
    list=card.cardsForUser(user_id)
    return { 'card': list }
@app.route('/api/card/<car_id>', methods=['GET'])
def get_card(car_id):
    card=CardModel()
    list=card.cardsById(int(car_id))
    return { 'card': list }

@app.route('/api/card', methods=['POST'])
def add_card():
    card_data = request.get_json()
    print("post card:", card_data)
    card = CardModel()
    resp=card.create(card_data)
    print("RESP", resp)
    if resp['status']==1:
        print("update token")
        user=UserModel()
        stat=user.updateToken(int(card_data['user_id']), -1)
        print("STAT:", stat)
    return resp, 201

@app.route('/api/card/<card_id>', methods=['PUT'])
def upgrade_card(card_id):
    card_data = request.get_json()
    print("put card:", card_data)
    card = CardModel()
    resp=card.update(card_data, card_id)
    return resp, 201

@app.route('/api/card/<card_id>', methods=['DELETE'])
def remove_card(card_id):
    card = CardModel()
    resp=card.delete(int(card_id))
    return resp, 201



# from flask import Flask,request
# from uuid import uuid4
# from flask.views import MethodView

# from schemas import CardSchema
# from db import card, users
# from . import bp
# from app import app
# # api = Blueprint('api',__name__, url_prefix='/api')

# @app.get('/api/card')
# def get_cards():
#   return { 'card': list(card.values()) }

# @app.get('/api/card/<card_id>')
# def get_card(card_id):
#     try:
#         return {'card': card[card_id]}, 200
#     except KeyError:
#         return {'message': "Invalid card"}, 400

# @app.post('/api/card/<card_id>')
# def add_card(card_id):
#   card_data = request.get_json()
#   user_id = card_data['user_id']
#   if user_id in users:
#     card[uuid4()] = card_data
#     return { 'message': "Card Added" }, 201
#   return { 'message': "Returned Card"}, 401

# @app.put('/api/card/<card_id>')
# def upgrade_card(card_id):
#     try:
#         c = card[card_id]
#         card_data = request.get_json()
#         if card_data['user_id'] == c['user_id']:
#             c['model'] = card_data['model']
#             return { 'message': 'Card Upgraded' }, 202
#         # return {'message': "Upgrade Unsuccessful"}, 401
#     except Exception as ex:
#         print(ex)
#         return {'message': "Not enough tokens"}, 400

# @app.delete('/api/card/<card_id>')
# def remove_card(card_id):
#   try:
#     del card[card_id]
#     return {"message": "Card Deleted"}, 202
#   except:
#     return {'message':"Invalid Card"}, 400