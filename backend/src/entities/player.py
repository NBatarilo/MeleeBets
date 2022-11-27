# coding=utf-8

from sqlalchemy import Column, String, Integer
from .entity import Entity, Base
from marshmallow import Schema, fields


class Player(Entity, Base):
    __tablename__ = 'players'

    player_name = Column(String)
    sponsor = Column(String)
    region = Column(String)

    def __init__(self, player_name, sponsor, region, created_by):
        Entity.__init__(self, created_by)
        self.player_name = player_name
        self.sponsor = sponsor
        self.region = region


class PlayerSchema(Schema):
    id = fields.Number()
    player_name = fields.Str()
    sponsor = fields.Str()
    region = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()