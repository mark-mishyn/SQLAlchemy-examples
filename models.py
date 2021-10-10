from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine("sqlite+pysqlite:///db.sqlite", echo=True, future=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    nickname = Column(String(30), unique=True)  # adds unique constrains
    fullname = Column(String)
    age = Column(Integer)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    addresses = relationship("Email", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, " \
               f"name={self.name!r}, " \
               f"fullname={self.fullname!r}, " \
               f"age={self.age})"


class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

