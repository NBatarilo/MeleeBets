from flask import Flask, jsonify, request
from sqlalchemy import select
from .models import Session
from .auth import AuthError, requires_auth

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
@requires_auth
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

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response