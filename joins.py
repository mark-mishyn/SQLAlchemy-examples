from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, joinedload, contains_eager
from sqlalchemy.orm import relationship

engine = create_engine("sqlite+pysqlite://", echo=True, future=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    emails = relationship('Email', back_populates='user')

    def __repr__(self):
        return self.name


class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='emails')

    def __repr__(self):
        return self.email


session = sessionmaker(bind=engine)()
Base.metadata.create_all(engine)


a = User(name='Eduard')
session.add(a)
session.add(Email(email='test1@example.net', user=a))
session.add(Email(email='test2@example.com', user=a))

b = User(name='Pedro')
session.add(Email(email='test3@example.net', user=b))
session.add(Email(email='test4@example.com', user=b))

session.commit()


print('users:::', session.query(User).count())
print('emails:::', session.query(Email).count())


def example_1():
    """SELECT ... FROM emails JOIN users"""
    for e, u in session.query(Email, User).join(User):
        print(e.email, u.name)


def example_2():
    """SELECT ... FROM users LEFT OUTER JOIN emails: result -- like prefetch_related"""
    for u in session.query(User).options(joinedload(User.emails)):
        print(u.name, [a.email for a in u.emails])


def example_3():
    """SELECT ... FROM users JOIN emails; result -- like prefetch_related"""
    for u in session.query(User).join(User.emails).options(contains_eager(User.emails)):
        print(u.name, [a.email for a in u.emails])


def example_4():
    """The same as before, but with filtered emails"""
    query = session.query(User).\
        join(User.emails).\
        options(contains_eager(User.emails)).\
        filter(Email.email.like('%.net'))

    for u in query:
        print(u, [a.email for a in u.emails])


def example_5():
    """Filter users by emails"""
    for u in session.query(User).join(User.emails).filter(Email.email == 'test1@example.net'):
        print(u)


def example_6():
    """Filter emails by users"""
    for a in session.query(Email).join(Email.user).filter(User.name == 'Pedro'):
        print(a)


example_6()
