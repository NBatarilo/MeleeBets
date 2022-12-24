from flask import jsonify, request, make_response
from src.auth import AuthError, requires_auth

from flask import Blueprint
from flask import current_app as app
from src.models import db, User, Player, Tournament, Bet, UserBet, BetSchema
#from flask_sqlalchemy import 


tests_bp = Blueprint(
    'tests_bp', __name__
)
"""
Example JSON:
{
    "User": {
        "username": "test_user",
        "password": "test_pass",
        "email": "test_email",
        "points": 0,
        "created_by": "populate_db"
    },

    "Player_One": {
        "player_name": "test_p1",
        "sponsor": "test_sponsor",
        "region": "NA-EAST",
        "created_by": "populate_db"
    },

    "Player_Two": {
        "player_name": "test_p2",
        "sponsor": "test_sponsor",
        "region": "NA-WEST",
        "created_by": "populate_db"
    },

    "Tournament": {
        "tournament_name": "Test Tournament V",
        "tournament_date_start": "11/11/11",
        "tournament_date_end": "11/13/11",
        "tournament_slug": "test-tournament-v",
        "entrants_number": 69,
        "tournament_type": "Major",
        "created_by": "populate_db"
    },

    "Matchup": {
        "player_one_id": 1,
        "player_two_id": 2,
        "created_by": "populate_db"
    },

    "Bet": {
        "odds": 420,
        "bet_type": "moneyline",
        "tournament_id": 1,
        "matchup_id": 1,
        "to_win": 1,
        "created_by": "populate_db"
    },

    "TournamentMatch": {
        "tournament_id": 1,
        "matchup_id": 1,
        "round": "Losers Round 3",
        "outcome": 0,
        "created_by": "populate_db"
    },

    "UserBet": {
        "user_id": 1,
        "bet_id": 1,
        "amount": 9001,
        "payout": 9002,
        "created_by": "populate_db"
    }
}

"""

@tests_bp.route('/test/populate_db', methods=['POST'])
def populate_db():
    #Add user
    User_dict = request.json['User']
    username = User_dict['username']
    email = User_dict['email']
    password = User_dict['password']
    points = User_dict['points']
    created_by = User_dict['created_by']
    new_user = User(
        username = username,
        password = password,
        email = email,
        points = points,
        created_by = created_by
    )
    db.session.add(new_user)

    #Add p1 and p2
    PlayerOne_dict = request.json['Player_One']
    PlayerTwo_dict = request.json['Player_Two']

    playerone_name = PlayerOne_dict["player_name"]
    sponsor = PlayerOne_dict["sponsor"]
    region = PlayerOne_dict["region"]
    created_by = PlayerOne_dict["created_by"]

    new_playerOne = Player(
        player_name=  playerone_name,
        sponsor=sponsor,
        region=region,
        created_by=created_by
    )
    db.session.add(new_playerOne)

    playertwo_name = PlayerTwo_dict["player_name"]
    sponsor = PlayerTwo_dict["sponsor"]
    region = PlayerTwo_dict["region"]
    created_by = PlayerTwo_dict["created_by"]

    new_playerTwo = Player(
        player_name=  playertwo_name,
        sponsor=sponsor,
        region=region,
        created_by=created_by
    )
    db.session.add(new_playerTwo)

    #Add tournament
    Tournament_dict = request.json['Tournament']
    tournament_name = Tournament_dict['tournament_name']
    tournament_date_start = Tournament_dict['tournament_date_start']
    tournament_date_end = Tournament_dict['tournament_date_end']
    tournament_slug = Tournament_dict['tournament_slug']
    entrants_number = Tournament_dict['entrants_number']
    tournament_type = Tournament_dict['tournament_type']

    new_Tournament = Tournament(
        tournament_name = tournament_name,
        tournament_date_start = tournament_date_start,
        tournament_date_end = tournament_date_end,
        tournament_slug = tournament_slug,
        entrants_number = entrants_number,
        tournament_type = tournament_type,
        created_by = created_by
    )
    db.session.add(new_Tournament)

    #Add matchup
    Matchup_dict = request.json['Matchup']
    player_one_id = Matchup_dict['player_one_id']
    player_two_id = Matchup_dict['player_two_id']

    new_Matchup = Matchup(
        player_one_id = player_one_id,
        player_two_id = player_two_id,
        created_by = created_by
    )
    db.session.add(new_Matchup)

    #Add bet
    Bet_dict = request.json['Bet']
    odds = Bet_dict['odds']
    bet_type = Bet_dict['bet_type']
    tournament_id = Bet_dict['tournament_id']
    matchup_id = Bet_dict['matchup_id']
    to_win = Bet_dict['to_win']
    new_Bet = Bet(
        odds = odds,
        bet_type = bet_type,
        tournament_id = tournament_id,
        matchup_id = matchup_id,
        to_win = to_win,
        created_by = created_by
    )
    db.session.add(new_Bet)

    #Add tournamentMatch
    TournamentMatch_dict = request.json['TournamentMatch']
    tournament_id = TournamentMatch_dict['tournament_id']
    matchup_id = TournamentMatch_dict['matchup_id']
    round = TournamentMatch_dict['round']
    outcome = TournamentMatch_dict['outcome']
    new_TournamentMatch = TournamentMatch(
        tournament_id = tournament_id,
        matchup_id = matchup_id,
        round = round,
        outcome = outcome,
        created_by = created_by
    )
    db.session.add(new_TournamentMatch)

    #Add UserBet
    UserBet_dict = request.json['UserBet']
    user_id = UserBet_dict['user_id']
    bet_id = UserBet_dict['bet_id']
    amount = UserBet_dict['amount']
    payout = UserBet_dict['payout']
    new_UserBet = UserBet(
        user_id = user_id,
        bet_id = bet_id,
        amount = amount,
        payout = payout,
        created_by = created_by
    )
    db.session.add(new_UserBet)

    db.session.commit()
    return make_response(f"New db info added: {new_user, new_playerOne, new_playerTwo, new_Tournament, new_Matchup, new_Bet, new_TournamentMatch, new_UserBet}")

@tests_bp.route('/test/get_Tournament_Bets/<tournament_slug>', methods=['GET'])
def get_TournamentBets(tournament_slug):

    #result = db.session.query(TournamentMatch, Tournament, Matchup, Player).join(TournamentMatch.tournaments).join(TournamentMatch.matchups)\
    #.join(Matchup.player_one).join(Matchup.player_two).filter(Tournament.tournament_slug == tournament_slug)

    PlayerOne = db.aliased(Player)
    PlayerTwo = db.aliased(Player)
    query = db.session.query(Bet, Tournament, Matchup, PlayerOne, PlayerTwo).join(Bet.tournaments).join(Bet.matchups)\
    .join(PlayerOne, Matchup.player_one).join(PlayerTwo, Matchup.player_two).filter(Tournament.tournament_slug == tournament_slug).all()

    print(query)
    result = BetSchema().dump(query)
    print(result)

    #bet = Bet.query.first()
    #return jsonify(BetSchema().dump(bet))

    #This logic works with schema
    bets = db.session.query(Bet).join(Bet.tournaments).filter(Tournament.tournament_slug == tournament_slug).all()

    #headers = {"Content-Type": "application/json"}
    return make_response(
        jsonify(BetSchema(many=True).dump(bets)),
        200
    )






