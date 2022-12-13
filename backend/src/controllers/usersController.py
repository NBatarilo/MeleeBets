from flask import jsonify, request, make_response
from src.auth import AuthError, requires_auth

from flask import Blueprint
from flask import current_app as app
from src.models import db, User
#from flask_sqlalchemy import 


users_bp = Blueprint(
    'users_bp', __name__
)


@users_bp.route('/users', methods=['GET'])
def add_users():
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')

    if username and email:
        new_user = User(
            username = username,
            password = password,
            email = email,
            points = 0,
            created_by="Test"
        )
        db.session.add(new_user)  # 
        db.session.commit()
        return make_response(f"New user info: {new_user}")

"""
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
"""