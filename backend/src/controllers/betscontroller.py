from flask import Flask, jsonify, request
from sqlalchemy import select
from .models import Session
from .auth import AuthError, requires_auth

@app.route('/bets')
def get_bets():
    
    session = Session()
    bet_objects = session.query(Bet).all()

    
    schema = BetSchema(many=True)
    bets = schema.dump(bet_objects)

    
    session.close()
    return jsonify(bets)


#Needs to be updated based on new schema
@app.route('/bets', methods=['POST'])
@requires_auth
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

#Is this necessary again?
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
