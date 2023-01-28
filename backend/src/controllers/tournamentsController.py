import requests
from flask import Flask, jsonify, request, make_response, Blueprint
from src.auth import AuthError, requires_auth
from flask import current_app as app
from src.models import db, User, Player, Set, Tournament, Bet, UserBet, BetSchema, TournamentSchema
from datetime import datetime

tournaments_bp = Blueprint(
    'tournaments_bp', __name__
)

@tournaments_bp.route('/api/tournaments/<tournament_slug>', methods = ['GET'])
def get_tournament(tournament_slug):
    #Probably going to make this "get_tournaments" and give a date range as input eventually
    #Also TODO: Add post method and make this a more general tourney db interaction function. if get:, if post: 

    tournament = db.session.query(Tournament).filter(Tournament.tournament_slug == tournament_slug).first()
    tournament_result = TournamentSchema().dump(tournament)
    return jsonify(tournament_result)

