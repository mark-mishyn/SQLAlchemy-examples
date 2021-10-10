from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from examples.models import Email, User


class UserFlatSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


class AddressFlatSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Email
        include_fk = True
        load_instance = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

    addresses = Nested(AddressFlatSchema, many=True, exclude=('user_id',))


class AddressSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Email
        include_fk = True
        load_instance = True

    user = Nested(UserFlatSchema, exclude=('addresses',))


