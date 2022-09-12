# coding=utf-8

from sqlalchemy import Column, String
from .entity import Entity, Base
from marshmallow import Schema, fields


class Match(Entity, Base):
    __tablename__ = 'matches'

    player_one = Column(String)
    player_two = Column(String)

    def __init__(self, player_one, player_two, created_by):
        Entity.__init__(self, created_by)
        self.player_one = player_one
        self.player_two = player_two


class MatchSchema(Schema):
    id = fields.Number()
    player_one = fields.Str()
    player_two = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()