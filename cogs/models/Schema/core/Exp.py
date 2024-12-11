from marshmallow import (EXCLUDE, fields, Schema, validates, validate, ValidationError)
from marshmallow import (post_dump, post_load, pre_dump, pre_load, pprint, INCLUDE)
import arrow



class Exp():
    def __init__(self, lvl, exp):
        self.lvl = lvl
        self.exp = exp

class ExpSchema(Schema):
    lvl = fields.Integer()
    exp = fields.Number()

    @post_load
    def make(self, data, **kwargs):
        return Exp(**data)

