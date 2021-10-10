from pprint import pprint

from examples.models import session, User, Email
from schemas import UserSchema, AddressSchema

user = session.query(User).get(1)
pprint(UserSchema().dump(user))

address = session.query(Email).first()
pprint(AddressSchema().dump(address))
# pprint(UserSchema().dump(session.query(User)[:20]), many=True)
