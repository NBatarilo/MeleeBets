from . import db, ma
from datetime import datetime
from sqlalchemy import ForeignKey



#Any relationship needs a nested schema


#Define users table
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    points = db.Column(db.Integer)

    def __init__(self, name, password, email, points, created_by):
        self.created_at = db.DateTime.now()
        self.updated_at = db.DateTime.now()
        self.last_updated_by = created_by
        self.name = name
        self.password = password
        self.email = email
        self.points = points


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

#Define players table
class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    player_name = db.Column(db.String)
    sponsor = db.Column(db.String)
    region = db.Column(db.String)


    def __init__(self, player_name, sponsor, region, created_by):
        self.created_at = db.DateTime.now()
        self.updated_at = db.DateTime.now()
        self.last_updated_by = created_by
        self.player_name = player_name
        self.sponsor = sponsor
        self.region = region


class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player

#Define tournaments table
class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    tournament_name = db.Column(db.String)
    tournament_date_start = db.Column(db.String)
    tournament_date_end = db.Column(db.String)
    tournament_slug = db.Column(db.String)
    entrants_number = db.Column(db.Integer)
    tournament_type = db.Column(db.String)

    def __init__(self, tournament_name, tournament_date_start, tournament_date_end, tournament_slug, entrants_number, tournament_type, created_by):
        self.created_at = db.DateTime.now()
        self.updated_at = db.DateTime.now()
        self.last_updated_by = created_by
        self.tournament_name = tournament_name
        self.tournament_date_start = tournament_date_start
        self.tournament_date_end = tournament_date_end
        self.tournament_slug = tournament_slug
        self.entrants_number = entrants_number
        self.tournament_type = tournament_type


class TournamentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tournament


#Define matchups table 
class Matchup(db.Model):
    __tablename__ = 'matchups'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    player_one_id = db.Column(db.Integer, ForeignKey("players.id"))
    player_two_id = db.Column(db.Integer, ForeignKey("players.id"))

    player_one = db.relationship("Player", foreign_keys = [player_one_id])
    player_two = db.relationship("Player", foreign_keys = [player_two_id])
    

    def __init__(self, player_one_id, player_two_id, created_by):
        self.created_at = db.DateTime.now()
        self.updated_at = db.DateTime.now()
        self.last_updated_by = created_by
        self.player_one_id = player_one_id
        self.player_two_id = player_two_id


class MatchupSchema(ma.SQLAlchemyAutoSchema):
    player_one = ma.Nested(PlayerSchema)
    player_two = ma.Nested(PlayerSchema)
    class Meta:
        model = Matchup
        

    #Define bets table
class Bet(db.Model):
    __tablename__ = 'bets'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    odds = db.Column(db.Integer)
    bet_type = db.Column(db.String)
    tournament_id = db.Column(db.Integer, ForeignKey("tournaments.id"))
    matchup_id = db.Column(db.Integer, ForeignKey("matchups.id"))
    status = db.Column(db.String)
    to_win = db.Column(db.Integer)

    tournaments = db.relationship("Tournament")
    matchups = db.relationship("Matchup")
    def __init__(self, odds, bet_type, tournament_id, matchup_id, to_win, created_by):
        self.created_at = db.DateTime.now()
        self.updated_at = db.DateTime.now()
        self.last_updated_by = created_by
        self.odds = odds
        self.bet_type = bet_type
        self.tournament_id = tournament_id
        self.matchup_id = matchup_id
        self.status = "open"
        self.to_win = to_win

class BetSchema(ma.SQLAlchemyAutoSchema):
    tournaments = ma.Nested(TournamentSchema)
    matchups = ma.Nested(MatchupSchema)
    class Meta:
        model = Bet
    

#Really need to drill down on this structure - tempted to merge this with bets table
#Define tournament_matches table
class TournamentMatch(db.Model):
    __tablename__ = 'tournament_matches'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    tournament_id = db.Column(db.Integer, ForeignKey("tournaments.id"))
    matchup_id = db.Column(db.Integer, ForeignKey("matchups.id"))
    round = db.Column(db.String)
    outcome = db.Column(db.Integer)

    tournaments = db.relationship("Tournament")
    matchups = db.relationship("Matchup")

    def __init__(self, tournament_id, matchup_id, round, outcome, created_by):
        
        self.created_at = db.DateTime.now()
        self.updated_at = db.DateTime.now()
        self.last_updated_by = created_by
        self.tournament_id = tournament_id
        self.matchup_id = matchup_id
        self.round = round
        self.outcome = outcome


class TournamentMatchSchema(ma.SQLAlchemyAutoSchema):
    tournaments = ma.Nested(TournamentSchema)
    matchups = ma.Nested(MatchupSchema)
    class Meta:
        model = TournamentMatch
    

#Define user_bets table
class UserBet(db.Model):
    __tablename__ = 'user_bets'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey("users.id"))
    bet_id = db.Column(db.Integer, ForeignKey("bets.id"))
    amount = db.Column(db.Integer)
    payout = db.Column(db.Integer)
    bet_result = db.Column(db.Integer)

    users = db.relationship("User")
    bets = db.relationship("Bet")
    

    def __init__(self, user_id, bet_id, amount, payout, created_by):
        self.created_at = db.DateTime.now()
        self.updated_at = db.DateTime.now()
        self.last_updated_by = created_by
        self.user_id = user_id
        self.bet_id = bet_id
        self.amount = amount
        self.payout = payout
        self.bet_result = -1



class UserBetSchema(ma.SQLAlchemyAutoSchema):
    users = ma.Nested(UserSchema)
    bets = ma.Nested(BetSchema)
    class Meta:
        model = UserBet