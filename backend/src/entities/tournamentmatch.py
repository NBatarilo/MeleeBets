# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from .entity import Entity, Base
from marshmallow import Schema, fields


class TournamentMatch(Entity, Base):
    __tablename__ = 'tournament_matches'

    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    matchup_id = Column(Integer, ForeignKey("matchups.id"))
    round = Column(String)
    outcome = Column(Integer)

    def __init__(self, tournament_id, matchup_id, round, outcome, created_by):
        Entity.__init__(self, created_by)
        self.tournament_id = tournament_id
        self.matchup_id = matchup_id
        self.round = round
        self.outcome = outcome


class TournamentMatchSchema(Schema):
    id = fields.Number()
    tournament_id = fields.Number()
    matchup_id = fields.Number()
    round = fields.Str()
    outcome = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()