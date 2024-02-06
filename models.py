
class Card:
  def __init__(self, year, make, model, rarity):
    self.year = year
    self.make = make
    self.model = model
    self.rarity = rarity

  def __repr__(self):
    return '<make {}>'.format(self.make)

  def classifications(self):
    return {
      'year': self.year,
      'make': self.make,
      'model': self.model,
      'rarity':self.rarity
    }