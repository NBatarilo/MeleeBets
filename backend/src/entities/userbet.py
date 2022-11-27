# coding=utf-8

from sqlalchemy import Column, Float, Integer
from .entity import Entity, Base
from marshmallow import Schema, fields


class UserBet(Entity, Base):
    __tablename__ = 'user_bets'

    user_id = Column(Integer)
    bet_id = Column(Integer)
    amount = Column(Float)
    payout = Column(Float)
    bet_result = Column(Integer)
    

    def __init__(self, user_id, bet_id, amount, payout, created_by):
        Entity.__init__(self, created_by)
        self.user_id = user_id
        self.bet_id = bet_id
        self.amount = amount
        self.payout = payout
        self.bet_result = -1



class UserBetSchema(Schema):
    id = fields.Number()
    user_id = fields.Number()
    bet_id = fields.Number()
    amount = fields.Float()
    payout = fields.Float()
    bet_result = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()