# coding=utf-8

from sqlalchemy import Column, String, Integer
from .entity import Entity, Base
from marshmallow import Schema, fields


class Tournament(Entity, Base):
    __tablename__ = 'tournaments'

    tournament_name = Column(String)
    tournament_date_start = Column(String)
    tournament_date_end = Column(String)
    tournament_slug = Column(String)
    entrants_number = Column(Integer)
    tournament_type = Column(String)

    def __init__(self, tournament_name, tournament_date_start, tournament_date_end, tournament_slug, entrants_number, tournament_type, created_by):
        Entity.__init__(self, created_by)
        self.tournament_name = tournament_name
        self.tournament_date_start = tournament_date_start
        self.tournament_date_end = tournament_date_end
        self.tournament_slug = tournament_slug
        self.entrants_number = entrants_number
        self.tournament_type = tournament_type


class TournamentSchema(Schema):
    id = fields.Number()
    tournament_name = fields.Str()
    tournament_date_start = fields.Str()
    tournament_date_end = fields.Str()
    tournament_slug = fields.Str()
    entrants_number = fields.Number()
    tournament_type = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()