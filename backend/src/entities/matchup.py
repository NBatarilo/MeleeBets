# coding=utf-8

from sqlalchemy import Column, String, Integer
from .entity import Entity, Base
from marshmallow import Schema, fields


class Matchup(Entity, Base):
    __tablename__ = 'matchups'

    player_one_id = Column(Integer)
    player_two_id = Column(Integer)
    

    def __init__(self, player_one_id, player_two_id, created_by, outcome):
        Entity.__init__(self, created_by)
        self.player_one_id = player_one_id
        self.player_two_id = player_two_id


class MatchupSchema(Schema):
    id = fields.Number()
    player_one_id = fields.Number()
    player_two_id = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()