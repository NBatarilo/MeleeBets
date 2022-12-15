from flask import jsonify, request, make_response
from src.auth import AuthError, requires_auth

from flask import Blueprint
from flask import current_app as app
from src.models import db, User, Player, Tournament, Matchup, Bet, TournamentMatch, UserBet
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
    }

    "Player_One": {
        "player_name": "test_p1",
        "sponsor": "test_sponsor",
        "region": "NA-EAST",
        "created_by": "populate_db"
    }

    "Player_Two": {
        "player_name": "test_p2",
        "sponsor": "test_sponsor",
        "region": "NA-WEST",
        "created_by": "populate_db"
    }

    "Tournament": {
        "tournament_name": "Test Tournament V",
        "tournament_date_start": "11/11/11",
        "tournament_date_end": "11/13/11",
        "tournament_slug": "test-tournament-v",
        "entrants_number": 69,
        "tournament_type": "Major",
        "created_by": "populate_db"
    }

    "Matchup": {
        "player_one_id": 1,
        "player_two_id": 2,
        "created_by": "populate_db"
    }

    "Bet": {
        "odds": 420,
        "bet_type": "moneyline",
        "tournament_id": 1,
        "matchup_id": 1,
        "to_win": 1,
        "created_by": "populate_db"
    }

    "TournamentMatch": {
        "tournament_id": 1,
        "matchup_id": 1,
        "round": "Losers Round 3",
        "outcome": 0,
        "created_by": "populate_db"
    }

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
def add_users():
    #Add user
    User_dict = request.json['User']
    username = User_dict[username]
    email = User_dict[email]
    password = User_dict[password]
    points = User_dict[points]
    created_by = User_dict[created_by]
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
        tournament_type = tournament_type
    )
    db.session.add(new_Tournament)

    #Add matchup
    


    db.session.commit()
    return make_response(f"New db info added: {new_user, new_playerOne, new_playerTwo}")
