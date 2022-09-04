# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.user import User

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
users = session.query(User).all()

if len(users) == 0:
    # create and persist mock exam
    example_user = User("Example Username", "salted and hashed password", "script")
    session.add(example_user)
    session.commit()
    session.close()

    # reload exams
    users = session.query(User).all()

# show existing exams
print('### USERS:')
for user in users:
    print(f'{user.id}, {user.name}, {user.password}')