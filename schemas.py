from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  email = fields.Str(required = True)
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )
  first_name = fields.Str()
  last_name = fields.Str()
  tokens = fields.Int()


class CardSchema(Schema):
  id = fields.Str(dump_only = True)
  year = fields.Str(required = True)
  make = fields.Str(required= True)
  model = fields.Str(required = True)

