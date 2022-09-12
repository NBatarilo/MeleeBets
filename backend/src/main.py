# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema
from .entities.match import Match, MatchSchema
from .entities.bet import Bet, BetSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/users')
def get_users():
    # fetching from the database
    session = Session()
    user_objects = session.query(User).all()

    # transforming into JSON-serializable objects
    schema = UserSchema(many=True)
    users = schema.dump(user_objects)

    # serializing as JSON
    session.close()
    return jsonify(users)


@app.route('/users', methods=['POST'])
def add_user():
    # mount user object
    posted_user = UserSchema(only=('name', 'password'))\
        .load(request.get_json())

    user = User(posted_user["name"], posted_user["password"], created_by="HTTP post request")
 
    # persist user
    session = Session()
    session.add(user)
    session.commit()

    # return created user
    new_user = UserSchema().dump(user)
    session.close()
    return jsonify(new_user), 201



@app.route('/matches')
def get_matches():
    
    session = Session()
    match_objects = session.query(Match).all()

    
    schema = MatchSchema(many=True)
    matches = schema.dump(match_objects)

    
    session.close()
    return jsonify(matches)


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
    


@app.route('/bets')
def get_bets():
    
    session = Session()
    bet_objects = session.query(Bet).all()

    
    schema = BetSchema(many=True)
    bets = schema.dump(bet_objects)

    
    session.close()
    return jsonify(bets)


@app.route('/bets', methods=['POST'])
def add_bet():
   
    posted_bet = BetSchema(only=('bettor_userid', 'bettor_username', 'odds', 'amount'))\
        .load(request.get_json())

    bet = Bet(posted_bet["bettor_userid"], posted_bet["bettor_username"], 
        posted_bet["odds"], posted_bet["amount"], created_by="HTTP post request")
 
    
    session = Session()
    session.add(bet)
    session.commit()

    
    new_bet = BetSchema().dump(bet)
    session.close()
    return jsonify(new_bet), 201