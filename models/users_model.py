from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), nullable = False, unique = True)
  email = db.Column(db.String(75), nullable = False, unique = True)
  password_hash = db.Column(db.String(250), nullable = False )
  first_name = db.Column(db.String(30))
  last_name = db.Column(db.String(30))
  tokens = db.Column(db.Integer, nullable = True)

  def __repr__(self):
    return f'<User: {self.username}>'

  def toJson(self):
    return {'id':self.id, 'username':self.username, 'email':self.email, 'first_name':self.first_name, 'last_name':self.last_name, 'tokens': self.tokens}
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def user(self, id):
    try:
      u =db.session.query(UserModel).get(id)
      return u.toJson()
    except:
      return {'message':'error finding user'}
  def users(self):
    temp=db.session.query(UserModel).all()
    users=[]
    for user in temp:
      users.append(user.toJson())
    return users

  def create(self, u):
    try:
      pwd = u['password']
 
      pwd=generate_password_hash(pwd)
      temp =UserModel(username=u['username'], email=u['email'], password_hash= pwd, tokens=u['tokens'])
      db.session.add(temp)
      db.session.commit()
      un=u['username']
      return { 'message' : f'{un} created'}
    except Exception as e:
      print(e)
      return { 'message' : 'Error creating user'}

  def update(self, u, id):
    try:
      print (id, " update:", u)
      db.session.query(UserModel).filter(id==id).update(u)
      db.session.commit()
      un=u['username']
      return { 'message' : f'{un} created'}
    except:
      return { 'message' : 'Error creating user'}

  def delete(self, id):
    try:
      db.session.query(UserModel).filter(id==id).delete()
      db.session.commit()
      return { 'message' : f'user {id} created'}
    except:
      return { 'message' : 'Error deleting user'}

  def from_dict(self, user_dict):
    for k, v in user_dict.items():
      if k != 'password':
        setattr(self, k, v)
      else:
        setattr(self, 'password_hash', generate_password_hash(v))