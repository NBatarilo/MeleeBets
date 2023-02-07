import requests
from flask import Flask, jsonify, request, make_response, Blueprint
from src.auth import AuthError, requires_auth
from flask import current_app as app
from src.models import db, User, Player, Set, Tournament, Bet, UserBet, BetSchema, TournamentSchema
from datetime import datetime

tournaments_bp = Blueprint(
    'tournaments_bp', __name__
)

@tournaments_bp.route('/api/tournaments/<tournament_slug>', methods = ['GET', 'POST'])
def tournament_db_api(tournament_slug):
    #Probably going to make this "get_tournaments" and give a date range as input eventually  
    if request.method == 'POST':
        #Add db post logic here
        return
    else:
        tournament = db.session.query(Tournament).filter(Tournament.tournament_slug == tournament_slug).first()
        tournament_result = TournamentSchema().dump(tournament)
        return jsonify(tournament_result)
    

#Also TODO: Move startgg tournament db POST functionality to this controller
#/api/tournaments/startgg/<tournament_slug>'

