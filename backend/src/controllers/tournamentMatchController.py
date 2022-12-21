from flask import Flask, jsonify, request
from src.auth import AuthError, requires_auth
from flask import Blueprint
from flask import current_app as app
from src.models import db, User, Player, Tournament, Matchup, Bet, TournamentMatch, UserBet, BetSchema

tournamentMatch_bp = Blueprint(
    'tournamentMatch_bp', __name__
)

@tournamentMatch_bp.route('/api/matches/<tournament_slug>', methods = ['GET'])
def get_tournament_matches(tournament_slug):
    print(Tournament.query.all())
    query = """
    SELECT some_fields FROM TOURNAMENTS AS T
    INNER JOIN TOURNAMENT_MATCHES AS TM ON T.ID = TM.TOURNAMENT_ID
    INNER JOIN BETS AS B ON B.MATCHUP_ID = TM.MATCHUP_ID
    WHERE T.TOURNAMENT_NAME = :slug
    """
    #What info to grab?
    #player_one name, player_two name, round, outcome, player_one sponsor, p2 sponsor

    #This is for getting all the bets for the tournament(?)
    #stmt = select(Tournament).join(Tournament.tournamentmatches).join(TournamentMatch.bets).join(Bet.matchups)
    #stmt = select(TournamentMatch, Tournament, Matchup, Player).join(TournamentMatch.tournaments).join(TournamentMatch.matchups)\
    #.join(Matchup.player_one).join(Matchup.player_two).where(Tournament.tournament_slug == tournament_slug)
    

@tournamentMatch_bp.route('/api/startgg/<tournament_slug>', methods = ['GET'])
def query_startgg(tournament_slug):
    #Read query into string from file

    #Build json payload/request and send request, jsonify response
    """
    import requests
 
    url = "https://httpbin.org/post"
    
    data = {
        "id": 1001,
        "name": "geek",
        "passion": "coding",
    }
    headers = { “Authorization” : ”our_unique_secret_token” }
    response = requests.post(url, json=data, headers = headers)
    
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())
    """

    #Iterate through data and format for entry
    return


#Legacy code - keeping for now for syntax. This functionality prob going to not be an endpoint
#Is this the best way to do this? Maybe remove POST method entirely and move further to back end
#Need to add authentication if it stays
"""
@app.route('/matches', methods=['POST'])
def add_matches():
    
    posted_matches = request.get_json()

    matches = posted_matches["matches_array"]
 
    
    session = Session()
    for match in matches:
        MatchSchema(only=('player_one', 'player_two')).load(match)
        session.add(Match(match["player_one"], match["player_two"], created_by="HTTP post request"))
    
    session.commit()

   
    new_match = MatchSchema().dump(Match(matches[0]["player_one"], matches[0]["player_two"], created_by="HTTP post request"))
    session.close()
    #Return first match inserted
    return jsonify(new_match), 201
"""
