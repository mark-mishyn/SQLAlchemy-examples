from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func, DateTime, delete
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine("sqlite+pysqlite://", echo=True, future=True)

Base = declarative_base()


def print_classes():
    print('classes')
    for c in session.query(Class):
        print(c.name)


def print_users():
    print('users')
    for u in session.query(User):
        print(u)


class ReprMixin:
    def __repr__(self):
        kw_str = ', '.join([f'{k}={getattr(self, k)}' for k in User.__table__.columns.keys()])
        return f'{self.__class__.__name__}({kw_str})'


class Class(Base):
    __tablename__ = 'classes'
    name = Column(String(30), primary_key=True)
    weight = Column(Integer)

    users = relationship('User', back_populates='user_class')


class User(ReprMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    lvl = Column(Integer, default=1)

    user_class_name = Column(Integer, ForeignKey('classes.name'))

    user_class = relationship('Class', back_populates='users')

    def level_up(self):
        """Race conditions safe update"""
        session.query(User).filter_by(id=self.id).update({'lvl': User.lvl + 1})
        session.commit()


Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

session.add_all([
    Class(name='Warrior', weight=100),
    Class(name='Assassin', weight=80),
    Class(name='Mage', weight=70),
    Class(name='Ranger', weight=75),
])

session.commit()

user1 = User(name='Mark', user_class=session.query(Class).first())

session.add(user1)
session.commit()

# regular update
user1.lvl += 1
session.commit()
# OR
# session.query(User).filter_by(id=user1.id).update({'lvl': User.lvl + 1})


user1.user_class = None
session.commit()

user1.level_up()

# delete user
u = session.get(User, 1)
session.delete(u)
# OR
# session.query(User).filter_by(id=10).delete()  # returns number of deleted objects

session.commit()

print(1111111)
print_users()

