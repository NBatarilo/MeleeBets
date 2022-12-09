from flask import Flask, jsonify, request
from sqlalchemy import select
from src.models import Session, Tournament, TournamentMatch, Bet, Matchup, Player
from src.auth import AuthError, requires_auth
from src.main import app, db, ma

@app.route('/api/matches/<tournament_slug>', methods = ['GET'])
def get_tournament_matches(tournament_slug):
    print(Tournament.query.all())
    query = """
    SELECT some_fields FROM TOURNAMENTS AS T
    INNER JOIN TOURNAMENT_MATCHES AS TM ON T.ID = TM.TOURNAMENT_ID
    INNER JOIN BETS AS B ON B.MATCHUP_ID = TM.MATCHUP_ID
    WHERE T.TOURNAMENT_NAME = :slug
    """
    #What info to grab?
    #player_one name, player_two name, round, outcome, player sponsors 

    #This is for getting all the bets for the tournament(?)
    #stmt = select(Tournament).join(Tournament.tournamentmatches).join(TournamentMatch.bets).join(Bet.matchups)
    stmt = select(Tournament).join(TournamentMatch).join(Matchup).join(Player).where(Tournament)
    
    result = session.execute()
    #tournament_match_objects = 

    #Look into make_response for returns 
    #headers = {"Content-Type": "application/json"}
    #return make_response(
        #'Test worked!', #Can also but something like jsonify(my_dict)
       #200,
       # headers=headers
    #)



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
