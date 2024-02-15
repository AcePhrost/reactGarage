from flask import request, session
from uuid import uuid4
from flask.views import MethodView
from models.users_model import UserModel

from functools import wraps
from . import bp
from db import users
from werkzeug.security import generate_password_hash, check_password_hash


from app import app
app.secret_key="My Big Secret"

def check_auth(username, password):
    user=UserModel()
    u=user.query.filter_by(username=username).first()
    print(u)
    if check_password_hash(u.password_hash, password):
        return True
    else:
        return False

def auth(username, password):
    user=UserModel()
    u=user.query.filter_by(username=username).first()
    print("auth", u)
    if check_password_hash(u.password_hash, password):
        return u
    else:
        return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return ({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)

    return decorated_function

def login_required1(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #auth = request.authorization

        if not auth or not check_auth(auth.username, auth.password):
            return ({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.post('/api/user/auth')
def auth_user():
    print ("post user")
    user_data = request.get_json()
    print("post user:", user_data)
    for k in ['username', 'password']:
        if k not in user_data:
            return { 'message' : 'Please include Username, Password'}, 400

    ##users[uuid4()] = user_data
    user = auth(user_data['username'], user_data['password'])
    if user==None:
        return {'status': -1, 'message': 'Failed authorization'}
    else:
        session['user']=user_data['username']
        session.permanent=True
        print ("session", session['user'])
        return {'status': 1, 'message': 'User authorized', 'user':user.toJson()}

    return resp, 201
@app.get('/api/user')
#@login_required
def user():
    user=UserModel()
    
    users=user.users()
    
    return users, 200

@app.get('/api/currentUser')
def currentUser():
    un=session['user']
    print ("UN", un)
    return us, 200
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