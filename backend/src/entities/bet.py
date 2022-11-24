# coding=utf-8

from sqlalchemy import Column, String, Float, Integer
from .entity import Entity, Base
from marshmallow import Schema, fields


class Bet(Entity, Base):
    __tablename__ = 'bets'

    bettor_userid = Column(String)
    bettor_username = Column(String)
    odds = Column(Float)
    amount = Column(Float)
    outcome = Column(String)
    payout = Column(Float)

    def __init__(self, bettor_userid, bettor_username, odds, amount, created_by):
        Entity.__init__(self, created_by)
        self.bettor_userid = bettor_userid
        self.bettor_username = bettor_username
        self.odds = odds
        self.amount = amount
        self.outcome = 'PENDING'
        self.payout = -1


class BetSchema(Schema):
    id = fields.Number()
    bettor_userid = fields.Int()
    bettor_username = fields.Str()
    odds = fields.Float()
    amount = fields.Float()
    outcome = fields.Str()
    payout = fields.Float()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()