from models import User, db_session, Email


# select all users
db_session.query(User)

# select all users and get list of them
db_session.query(User).all()

# count of users
db_session.query(User).count()
# or
db_session.query(User).filter(User.name == 'Eduard').count()

# list of users IDs
[v for v, in db_session.query(User.id)]

# get 1 user by ID (if no user, returns None)
db_session.query(User).get(1)
# or
db_session.get(User, 1)

# order users by fullname (slice returns list)
db_session.query(User).order_by(User.fullname)[:10]

# order users by multiple fields
db_session.query(User).order_by(User.name, User.nickname)[:10]

# order users by fullname desc
db_session.query(User).order_by(User.fullname.desc())[:10]

# filter by strict match
db_session.query(User).filter(User.name == 'Eduard').all()

# filter like name__iexact
db_session.query(User).filter(User.name.like('eduard')).all()

# filter like name__starswith
db_session.query(User).filter(User.name.like('Ed%')).all()

# filter like name__icontains
db_session.query(User).filter(User.nickname.like('%Wz%')).all()

# filter by great than
db_session.query(User).filter(User.age > 50)[:10]

# filter by IN operator
db_session.query(User).filter(User.id.in_([1, 2, 3, 4, 5]))[:10]

# short variant or several filters with strict match
db_session.query(User).filter_by(id=1, age=31).all()

# first object
db_session.query(User).filter_by(id=1, age=31).first()

# get only 1 OR None OR raise MultipleResultsFound
db_session.query(User).filter_by(age=31).scalar()

# filter emails by users
db_session.query(Email).join(Email.user).filter(User.name == 'Pedro')

# select specific fields only
# (NOTE: result type is query; it's iterable OR use query.all() to get list of tuples)
db_session.query(User.name, User.nickname).all()
