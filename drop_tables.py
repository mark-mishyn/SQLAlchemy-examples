from models import User, Email, engine

for model in (User, Email):
    try:
        model.__table__.drop(engine)
    except Exception as err:
        print(err)
