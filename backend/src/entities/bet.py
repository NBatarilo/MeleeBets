# coding=utf-8

from sqlalchemy import Column, Float, String, Integer, ForeignKey
from .entity import Entity, Base
from marshmallow import Schema, fields


class Bet(Entity, Base):
    __tablename__ = 'bets'

    odds = Column(Float)
    bet_type = Column(String)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    matchup_id = Column(Integer, ForeignKey("matchups.id"))
    status = Column(String)
    to_win = Column(Integer)

    def __init__(self, odds, bet_type, tournament_id, matchup_id, to_win, created_by):
        Entity.__init__(self, created_by)
        self.odds = odds
        self.bet_type = bet_type
        self.tournament_id = tournament_id
        self.matchup_id = matchup_id
        self.status = "open"
        self.to_win = to_win



class BetSchema(Schema):
    id = fields.Number()
    odds = fields.Float()
    bet_type = fields.String()
    tournament_id = fields.Number()
    matchup_id = fields.Number()
    status = fields.String()
    to_win = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()