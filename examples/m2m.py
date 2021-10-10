from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('sqlite+pysqlite:///db2.sqlite', echo=True, future=True)

Base = declarative_base()


class Association(Base):
    __tablename__ = 'association'

    parent_id = Column(Integer, ForeignKey('parents.id'), primary_key=True)
    child_id = Column(Integer, ForeignKey('children.id'), primary_key=True)

    child = relationship("Child", backref="parent_associations")
    parent = relationship("Parent", backref="child_associations")


class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    children = relationship("Child", secondary="association")

    def __repr__(self):
        return 'Parent ' + self.name


class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return 'Child ' + self.name


session = sessionmaker(bind=engine)()
Base.metadata.create_all(engine)

parent1 = Parent(name='Papito')
session.add(parent1)

child1 = Child(name='Alisa')
session.add(parent1)

parent1.children.append(child1)

session.commit()


for u in session.query(Parent):
    print(u, u.children)
