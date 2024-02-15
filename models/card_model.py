from app import db

class CardModel(db.Model):

  __tablename__ = 'cards'

  id = db.Column(db.Integer, primary_key = True)
  year = db.Column(db.String, nullable = False)
  make = db.Column(db.String, nullable = False)
  model = db.Column(db.String, nullable = False)
  user_id = db.Column(db.Integer, nullable = False)

  def __repr__(self):
      return '<make {}>'.format(self.make)

  def toJson(self):
      return {'id':self.id, 'year':self.year, 'make':self.make, 'model':self.model, 'userId':self.user_id}

  def commit(self):
      db.session.add(self)
      db.session.commit()

  def cards(self):
      temp=db.session.query(CardModel).all()
      cards=[]
      for card in temp:
        cards.append(card.toJson())
      return cards

  def cardsForUser(self, userId):
      temp=db.session.query(CardModel).all()
      cards=[]
      userId=int(userId)
      for card in temp:
        if card.user_id==userId:
          cards.append(card.toJson())
      return cards
  def cardsById(self, carId):
      temp=db.session.query(CardModel).get(carId)
      json =temp.toJson()
      return json
  def create(self, c):

      card =CardModel(year=c['year'], make=c['make'], model=c['model'], user_id=c['user_id'])

      db.session.add(card)
      db.session.commit()
      
      return {'status':1, 'message' : f'card created'}
      #temp =UserModel(username=u['username'], email=u['email'], password_hash= pwd, tokens=u['tokens'])
        
  def update(self, c, id):
      try:
        print (id, " update:", c)
        db.session.query(CardModel).filter(id==id).update(c)
        db.session.commit()
      
        return { 'message' : f'card update'}
      except:
        return { 'message' : 'Error creating user'}

  def delete(self,carId):
    try:
      #db.session.delete(self)
      db.session.query(CardModel).filter_by(id=carId).delete()
      #car.delete()
        
      db.session.commit()
      return { 'message' : f'card deleted'}
    except:
      return { 'message' : 'Error deleting car'}
    # def __init__(self, year, make, model, rarity):
    #   self.year = year
    #   self.make = make
    #   self.model = model
    #   self.rarity = rarity

  

  # def classifications(self):
  #   return {
  #     'year': self.year,
  #     'make': self.make,
  #     'model': self.model,
  #     'rarity':self.rarity
  #   }
