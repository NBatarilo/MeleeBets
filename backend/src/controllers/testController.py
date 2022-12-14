from flask import jsonify, request, make_response
from src.auth import AuthError, requires_auth

from flask import Blueprint
from flask import current_app as app
from src.models import db, User
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
        "player_name": "test_p1"
        "sponsor": "test_sponsor"
        "region": "NA-EAST"
        "created_by": "populate_db"
    }
    "Player_Two": {
        "player_name": "test_p2"
        "sponsor": "test_sponsor"
        "region": "NA-WEST"
        "created_by": "populate_db"
    }
    "Tournament": {
        tournament_name
tournament_date_start
tournament_date_end
tournament_slug
entrants_number
tournament_type
created_by
    }
    "Matchup":
    "Bet":
    "TournamentMatch":
    "UserBet":
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



    db.session.commit()
    return make_response(f"New user info: {new_user}")
