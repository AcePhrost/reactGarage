from flask import request
from uuid import uuid4
from flask.views import MethodView
from models.users_model import UserModel
from functools import wraps
from . import bp
from db import users
from werkzeug.security import generate_password_hash, check_password_hash


from app import app

def check_auth(username, password):
    user=UserModel()
    u=user.query.filter_by(username=username).first()
    print(u)
    chk=check_password_hash(u.password_hash, password)
    return username == u.username and chk

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return ({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.get('/api/user')
@login_required
def user():
    user=UserModel()
    users=user.users()
    
    return users, 200

@app.get('/api/user/<user_id>')
def get_user(user_id):
  try:
    request.h
    user=UserModel()
    u=user.user(user_id)
    return u
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

    ##users[uuid4()] = user_data
    user=UserModel()
    resp=user.create(user_data)
    return resp, 201

@app.put('/api/user/<user_id>')
def update_user(user_id):
    try:
        
        user_data = request.get_json()
        user=UserModel()
        resp=user.update(user_data, user_id)
        return { 'message': f'{user_data["username"]} updated'}, 202
    except KeyError:
        return {'message': "Invalid User"}, 400

@app.delete('/api/user/<user_id>')
def delete_user(user_id):
  # user_data = request.get_json()
  # username = user_data['username']
    try:
        user=UserModel()
        user.delete(user_id)
        return { 'message': f'User Deleted' }, 202
    except:
        return {'message': "Invalid username"}, 400