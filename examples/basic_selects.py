from models import User, session, Email


# select all users
session.query(User)

# select all users and get list of them
session.query(User).all()

# count of users
session.query(User).count()

# list of users IDs
[v for v, in session.query(User.id)[:10]]

# get 1 user by ID
session.query(User).get(1)
session.get(User, 1)

# order users by fullname
session.query(User).order_by(User.fullname)[:10]

# order users by multiple fields
session.query(User).order_by(User.name, User.nickname)[:10]

# order users by fullname desc
session.query(User).order_by(User.fullname.desc())[:10]

# filter by strict match
session.query(User).filter(User.name == 'Eduard').all()

# filter like name__iexact
session.query(User).filter(User.name.like('eduard')).all()

# filter like name__starswith
session.query(User).filter(User.name.like('Ed%')).all()

# filter like name__icontains
session.query(User).filter(User.nickname.like('%Wz%')).all()

# filter by great than
session.query(User).filter(User.age > 50)[:10]

# filter by IN operator
session.query(User).filter(User.id.in_([1, 2, 3, 4, 5]))[:10]

# short variant or several filters with strict match
session.query(User).filter_by(id=1, age=31).all()

# first object
session.query(User).filter_by(id=1, age=31).first()

# get only 1 OR None OR raise MultipleResultsFound
session.query(User).filter_by(age=31).scalar()

# filter emails by users
session.query(Email).join(Email.user).filter(User.name == 'Pedro')

# select specific fields only
# (NOTE: result type is query; it's iterable OR use query.all() to get list of tuples)
session.query(User.name, User.nickname).all()
