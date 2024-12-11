from marshmallow import (EXCLUDE, fields, Schema, validates, validate, ValidationError)
from marshmallow import (post_dump, post_load, pre_dump, pre_load, pprint, INCLUDE)
import arrow


class Staff():
    def __init__(self, enable=False, category=0):
        self.enable = enable
        self.category = category

class StaffSchema(Schema):
    enable = fields.Boolean()
    category = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return Staff(**data)