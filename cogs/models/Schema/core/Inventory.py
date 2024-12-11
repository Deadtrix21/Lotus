from marshmallow import (EXCLUDE, fields, Schema, validates, validate, ValidationError)
from marshmallow import (post_dump, post_load, pre_dump, pre_load, pprint, INCLUDE)
import arrow

class InventoryItem():
    def __init__(self):
        pass
    
class InventoryItemSchema(Schema):
    name = fields.String()

    #@post_load
    def make(self, data, **kwargs):
        return InventoryItem(**data)