# coding=utf-8

from sqlalchemy import Column, String
from .entity import Entity, Base
from marshmallow import Schema, fields


class User(Entity, Base):
    __tablename__ = 'users'

    name = Column(String)
    password = Column(String)

    def __init__(self, name, password, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.password = password


class UserSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    password = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()