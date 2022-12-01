# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from .models import Session, engine, Base
from sqlalchemy import select
from .auth import AuthError, requires_auth

# creating the Flask application
app = Flask(__name__)
app.debug = True
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run()

"""
@app.route('/test')
def get_test():
    return jsonify('test endpoint')

@app.route('/test-private')
@requires_auth
def get_test_private():
    return jsonify('test endpoint behind')
"""