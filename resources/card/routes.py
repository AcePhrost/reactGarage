from flask import Flask, request, jsonify
from uuid import uuid4
from db import card, users  # Assuming you have imported your data structures correctly
from app import app

@app.route('/api/card', methods=['GET'])
def get_cards():
    return jsonify({'card': list(card.values())}), 200

@app.route('/api/card/<card_id>', methods=['GET'])
def get_card(card_id):
    if card_id in card:
        return jsonify({'card': card[card_id]}), 200
    else:
        return jsonify({'message': "Invalid card"}), 400

@app.route('/api/card/<card_id>', methods=['POST'])
def add_card(card_id):
    card_data = request.get_json()
    user_id = card_data.get('user_id')  # Accessing user_id safely
    if user_id in users:
        card[card_id] = card_data  # Using the provided card_id
        return jsonify({'message': "Card Added"}), 201
    else:
        return jsonify({'message': "User not found"}), 401

@app.route('/api/card/<card_id>', methods=['PUT'])
def upgrade_card(card_id):
    if card_id in card:
        card_data = request.get_json()
        if card_data['user_id'] == card[card_id]['user_id']:
            card[card_id]['model'] = card_data['model']
            return jsonify({'message': 'Card Upgraded'}), 202
        else:
            return jsonify({'message': "Unauthorized"}), 401
    else:
        return jsonify({'message': "Card not found"}), 404

@app.route('/api/card/<card_id>', methods=['DELETE'])
def remove_card(card_id):
    if card_id in card:
        del card[card_id]
        return jsonify({"message": "Card Deleted"}), 202
    else:
        return jsonify({'message': "Invalid Card"}), 400



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