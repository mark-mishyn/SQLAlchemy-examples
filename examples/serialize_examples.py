from pprint import pprint

from examples.models import db_session, User, Email
from schemas import UserSchema, AddressSchema

user = db_session.query(User).get(1)
pprint(UserSchema().dump(user))

address = db_session.query(Email).first()
pprint(AddressSchema().dump(address))
# pprint(UserSchema().dump(session.query(User)[:20]), many=True)
