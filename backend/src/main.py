# coding=utf-8

from flask import Flask, jsonify, request
from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema

# creating the Flask application
app = Flask(__name__)

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