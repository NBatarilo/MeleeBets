from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from marshmallow import Schema, fields

# Configure and start db
db_url = 'localhost:5432'
db_name = 'melee-bets'
db_user = 'postgres'
db_password = 'secret'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

#Define base entity class for db (DEPRECATED)
"""
class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
"""

#Define users table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    name = Column(String)
    password = Column(String)
    email = Column(String)
    points = Column(Integer)

    def __init__(self, name, password, email, points, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.name = name
        self.password = password
        self.email = email
        self.points = points


class UserSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    password = fields.Str()
    email = fields.Str()
    points = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()

#Define players table
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    player_name = Column(String)
    sponsor = Column(String)
    region = Column(String)

    matchups = relationship("Matchup", back_popuplates = "players")

    def __init__(self, player_name, sponsor, region, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
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

#Define tournaments table
class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    tournament_name = Column(String)
    tournament_date_start = Column(String)
    tournament_date_end = Column(String)
    tournament_slug = Column(String)
    entrants_number = Column(Integer)
    tournament_type = Column(String)

    def __init__(self, tournament_name, tournament_date_start, tournament_date_end, tournament_slug, entrants_number, tournament_type, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
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


#Define matchups table 
class Matchup(Base):
    __tablename__ = 'matchups'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    player_one_id = Column(Integer, ForeignKey("players.id"))
    player_two_id = Column(Integer, ForeignKey("players.id"))
    player_one = Player()
    player_two = Player()

    #Might need to add second declaration if this doesn't work
    players = relationship("Player", back_popuplates = "matchup")
    

    def __init__(self, player_one_id, player_two_id, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.player_one_id = player_one_id
        self.player_two_id = player_two_id


class MatchupSchema(Schema):
    id = fields.Number()
    player_one_id = fields.Number()
    player_two_id = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
    player_one = fields.Nested(PlayerSchema)
    player_two = fields.Nested(PlayerSchema)


    #Define bets table
class Bet(Base):
    __tablename__ = 'bets'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    odds = Column(Float)
    bet_type = Column(String)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    matchup_id = Column(Integer, ForeignKey("matchups.id"))
    status = Column(String)
    to_win = Column(Integer)

    tournaments = relationship("Tournament", back_populates = "bets")
    matchups = relationship("Matchup", back_popuplates = "bets")

    def __init__(self, odds, bet_type, tournament_id, matchup_id, to_win, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
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
    

#Define tournament_matches table
class TournamentMatch(Base):
    __tablename__ = 'tournament_matches'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    matchup_id = Column(Integer, ForeignKey("matchups.id"))
    round = Column(String)
    outcome = Column(Integer)
    matchup = Matchup()

    tournaments = relationship("Tournament", back_populates = "tournament_matches")
    matchups = relationship("Matchup", back_popuplates = "tournament_matches")

    def __init__(self, tournament_id, matchup_id, round, outcome, created_by):
        
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
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
    matchup = fields.Nested(MatchupSchema)
    

#Define user_bets table
class UserBet(Entity, Base):
    __tablename__ = 'user_bets'

    user_id = Column(Integer, ForeignKey("users.id"))
    bet_id = Column(Integer, ForeignKey("bets.id"))
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