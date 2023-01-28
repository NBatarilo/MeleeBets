from . import db, ma
from datetime import datetime


#Define users table
class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = (
        db.UniqueConstraint('username'),
        db.UniqueConstraint('password'),
        db.UniqueConstraint('email'),
    )

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    points = db.Column(db.Integer)

    def __init__(self, username, password, email, points, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.username = username
        self.password = password
        self.email = email
        self.points = points

    def __repr__(self):
        return f"username:{self.username}, password:{self.password}, email:{self.email}"



class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

#Define players table
#One day need to deal with players with the same name - won't bne a problem for a while
class Player(db.Model):
    __tablename__ = 'players'
    __table_args__ = (
        db.UniqueConstraint('player_name'),
    )

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    player_name = db.Column(db.String)
    sponsor = db.Column(db.String)
    region = db.Column(db.String)



    def __init__(self, player_name, sponsor, region, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.player_name = player_name
        self.sponsor = sponsor
        self.region = region

    def __repr__(self):
        return f"player_name:{self.player_name}, sponsor:{self.sponsor}, region:{self.region}"


class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player



class Set(db.Model):
    __tablename__ = 'sets'
    __table_args__ = (
        db.UniqueConstraint('tournament_id', 'player_one_id', 'player_two_id', 'phase_id', 'full_round_text'),
    )
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id"))
    player_one_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    player_two_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    phase_id = db.Column(db.Integer)
    full_round_text = db.Column(db.String)
    round = db.Column(db.String)
    outcome = db.Column(db.Integer)
    identifier = db.Column(db.String)
    startgg_setID = db.Column(db.Integer)
    player_one_prereqID = db.Column(db.String)
    player_two_prereqID = db.Column(db.String)
    #Maybe also include prereqPlacement - prob don't need though

    player_one = db.relationship("Player", backref = "p1_sets", foreign_keys = [player_one_id])
    player_two = db.relationship("Player", backref = "p2_sets", foreign_keys = [player_two_id])

    def __init__(self, tournament_id, player_one_id, player_two_id, phase_id, round, identifer, startgg_setID, player_one_prereqID, player_two_prereqID, created_by):
        
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.tournament_id = tournament_id
        self.player_one_id = player_one_id
        self.player_two_id = player_two_id
        self.phase_id = phase_id
        self.round = round
        self.outcome = 0
        self.identifer = identifer
        self.startgg_setID = startgg_setID
        self.player_one_prereqID = player_one_prereqID
        self.player_two_prereqID = player_two_prereqID 


    def __repr__(self):
        return f"tournament_id:{self.tournament_id}, matchup_id:{self.full_round_text}, round:{self.player_one_id}"

class SetSchema(ma.SQLAlchemyAutoSchema):
    player_one = ma.Nested(PlayerSchema)
    player_two = ma.Nested(PlayerSchema)
    class Meta:
        model = Set



#Define tournaments table
#TODO: Add tournemant image to this
class Tournament(db.Model):
    __tablename__ = 'tournaments'
    __table_args__ = (
        db.UniqueConstraint('tournament_name'),
    )
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    tournament_name = db.Column(db.String)
    tournament_date_start = db.Column(db.String)
    tournament_date_end = db.Column(db.String)
    tournament_slug = db.Column(db.String)
    entrants_number = db.Column(db.Integer)
    tournament_type = db.Column(db.String)

    sets = db.relationship("Set", backref = "tournaments")

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

    def __repr__(self):
        return f"tournament_name:{self.tournament_name}, tournament_slug:{self.tournament_slug}, tournament_type:{self.tournament_type}"


class TournamentSchema(ma.SQLAlchemyAutoSchema):
    sets = ma.Nested(SetSchema)
    class Meta:
        model = Tournament



#Define bets table
class Bet(db.Model):
    __tablename__ = 'bets'
    __table_args__ = (
        db.UniqueConstraint('set_id', 'to_win'),
    )
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    odds = db.Column(db.Integer)
    bet_type = db.Column(db.String)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id"))
    set_id = db.Column(db.Integer, db.ForeignKey("sets.id"))
    status = db.Column(db.String)
    to_win = db.Column(db.Integer)

    tournament = db.relationship("Tournament", backref = "bets")
    set = db.relationship("Set", backref = "bets")

    def __init__(self, odds, bet_type, tournament_id, set_id, to_win, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.odds = odds
        self.bet_type = bet_type
        self.tournament_id = tournament_id
        self.set_id = set_id
        self.status = "open"
        self.to_win = to_win

    def __repr__(self):
        return f"odds:{self.odds}, bet_type:{self.bet_type}, status:{self.status}"


class BetSchema(ma.SQLAlchemyAutoSchema):
    set = ma.Nested(SetSchema)
    class Meta:
        model = Bet
    


#Define user_bets table
class UserBet(db.Model):
    __tablename__ = 'user_bets'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'bet_id'),
    )
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    bet_id = db.Column(db.Integer, db.ForeignKey("bets.id"))
    amount = db.Column(db.Integer)
    payout = db.Column(db.Integer)
    bet_result = db.Column(db.Integer)

    user = db.relationship("User", backref = 'user_bets')
    bets = db.relationship("Bet", backref = 'user_bets')
    

    def __init__(self, user_id, bet_id, amount, payout, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.user_id = user_id
        self.bet_id = bet_id
        self.amount = amount
        self.payout = payout
        self.bet_result = -1

    def __repr__(self):
        return f"user_id:{self.user_id}, bet_id:{self.bet_id}, amount:{self.amount}"



class UserBetSchema(ma.SQLAlchemyAutoSchema):
    user = ma.Nested(UserSchema)
    bets = ma.Nested(BetSchema)
    class Meta:
        model = UserBet

#Still not sure if this is the direction to take
"""
class SetNode():

    def __init__(self, Set):
        self.Set = Set
        self.winnerNextSet = None
        self.loserNextSet = None
        self.pOneLastSet = None
        self.pTwoLastSet = None
"""