from pprint import pprint

import sqlalchemy

from models import User, session, Email

# select all users
session.query(User)

# select all users and get list of them
session.query(User).all()

# count of users
pprint(session.query(User).count())

# list of users IDs
pprint([v for v, in session.query(User.id)[:10]])

# get 1 user by ID
session.query(User).get(1)
session.get(User, 1)

# order users by fullname
pprint(session.query(User).order_by(User.fullname)[:10])

# order users by multiple fields
pprint(session.query(User).order_by(User.name, User.nickname)[:10])

# order users by fullname desc
pprint(session.query(User).order_by(User.fullname.desc())[:10])

# filter by strict match
pprint(session.query(User).filter(User.name == 'Eduard').all())

# filter like name__iexact
pprint(session.query(User).filter(User.name.like('eduard')).all())

# filter like name__starswith
pprint(session.query(User).filter(User.name.like('Ed%')).all())

# filter like name__icontains
pprint(session.query(User).filter(User.nickname.like('%Wz%')).all())

# filter by great than
pprint(session.query(User).filter(User.age > 50)[:10])

# filter by IN operator
pprint(session.query(User).filter(User.id.in_([1, 2, 3, 4, 5]))[:10])

# short variant or several filters with strict match
pprint(session.query(User).filter_by(id=1, age=31).all())

# first object
pprint(session.query(User).filter_by(id=1, age=31).first())

# get only 1 OR None OR raise MultipleResultsFound
pprint(session.query(User).filter_by(age=31).scalar())

# filter emails by users
pprint(session.query(Email).join(Email.user).filter(User.name == 'Pedro'))

# select specific fields only
# (NOTE: result type is query; it's iterable OR use query.all() to get list of tuples)
session.query(User.name, User.nickname)
