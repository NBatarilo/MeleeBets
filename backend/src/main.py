# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from sqlalchemy import select
from .auth import AuthError, requires_auth
from .models import db, ma
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# creating the Flask application
app = Flask(__name__)
#Need to figure out how to route outside of main
app.debug = True
CORS(app)

#Configure db
db_url = 'localhost:5432'
db_name = 'melee-bets'
db_user = 'postgres'
db_password = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost:5432/melee-bets'
db.init_app(app)
ma.init_app(app)

if __name__ == "__main__":
    app.run()
    db.create_all()

"""
@app.route('/test')
def get_test():
    return jsonify('test endpoint')

@app.route('/test-private')
@requires_auth
def get_test_private():
    return jsonify('test endpoint behind')
"""