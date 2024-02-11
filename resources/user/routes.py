from flask import request
from uuid import uuid4
from flask.views import MethodView
from models.users_model import UserModel
from . import bp
from db import users

from app import app

@app.get('/api/user')
def user():
    users=UserModel.from_dict()
    print(users)
    return{'users': list(users.values())}, 200

@app.get('/api/user/<user_id>')
def get_user(user_id):
  try:
    return { 'user': users[user_id] } 
  except:
    return {'message': 'invalid user'}, 400

@app.post('/api/user')
def create_user():
    print ("post user")
    user_data = request.get_json()
    print("post user:", user_data)
    for k in ['username', 'email', 'password']:
        if k not in user_data:
            return { 'message' : 'Please include Username, Password, and Email'}, 400
    users[uuid4()] = user_data
    return { 'message' : f'{user_data["username"]} created'}, 201

@app.put('/api/user/<user_id>')
def update_user(user_id):
    try:
        user = users[user_id]
        user_data = request.get_json()
        user |= user_data
        return { 'message': f'{user["username"]} updated'}, 202
    except KeyError:
        return {'message': "Invalid User"}, 400

@app.delete('/api/user/<user_id>')
def delete_user(user_id):
  # user_data = request.get_json()
  # username = user_data['username']
    try:
        del users[user_id]
        return { 'message': f'User Deleted' }, 202
    except:
        return {'message': "Invalid username"}, 400