from app import db

class CardModel(db.Model):

  __tablename__ = 'cards'

  id = db.Column(db.Integer, primary_key = True)
  year = db.Column(db.String, nullable = False)
  make = db.Column(db.String, nullable = False)
  model = db.Column(db.String, nullable = False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

def __repr__(self):
    return '<make {}>'.format(self.make)

def commit(self):
    db.session.add(self)
    db.session.commit()

def delete(self):
  db.session.delete(self)
  db.session.commit()
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
