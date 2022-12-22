import requests
from flask import Flask, jsonify, request, make_response
from src.auth import AuthError, requires_auth
from flask import Blueprint
from flask import current_app as app
from src.models import db, User, Player, Tournament, Matchup, Bet, TournamentMatch, UserBet, BetSchema

tournamentMatch_bp = Blueprint(
    'tournamentMatch_bp', __name__
)

@tournamentMatch_bp.route('/api/matches/<tournament_slug>', methods = ['GET'])
def get_tournament_matches(tournament_slug):
    return
    #What info to grab?
    #player_one name, player_two name, round, outcome, player_one sponsor, p2 sponsor

    #This is for getting all the bets for the tournament(?)
    #stmt = select(Tournament).join(Tournament.tournamentmatches).join(TournamentMatch.bets).join(Bet.matchups)
    #stmt = select(TournamentMatch, Tournament, Matchup, Player).join(TournamentMatch.tournaments).join(TournamentMatch.matchups)\
    #.join(Matchup.player_one).join(Matchup.player_two).where(Tournament.tournament_slug == tournament_slug)
    

@tournamentMatch_bp.route('/api/startgg/<tournament_slug>', methods = ['GET'])
def query_startgg(tournament_slug):
    #Read query into string from file
    #TODO: Get phase ID's first, use last one to query for sets
    #Will be strictly getting top 8 from majors essentially. Read sets into db and query into tree for front end.
    #Could do SetNode object that has the set + parent set and children sets in list
    #ROUND AND IDENTIFIER WILL BE HUGE HERE. Gives us the tree structure
    with open('src/startggQueries/phaseSets.txt', 'r') as file:
        query = file.read().replace('<tournament_slug>', tournament_slug)

    #Build json payload/request and send request, jsonify response
    payload = {"query": query}
 
    url = "https://api.start.gg/gql/alpha"
    
    headers = {"Authorization" : "Bearer 3b70dc3e655754d9010c3ea829e81cd8"}
    response = requests.post(url, json=payload, headers = headers)
    
    
    return make_response(
        response.json(),
        response.status_code
    )

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
