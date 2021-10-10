import random

from models import User, Email, session
from utils import get_random_string

# delete rows
session.query(User).delete()
session.query(Email).delete()

session.add(User(name='Eduard', fullname='Ed Jones', age=31))
session.add(User(name='Pedro', fullname='Pedro Eagleasias', age=18))


session.bulk_save_objects([
    User(name='Roberto', fullname='Rob Shin', age=22),
    User(name='Hulio', fullname='Hulio Nado', age=10)
])


for i in range(1000):
    session.add(
        User(name=get_random_string().capitalize(),
             fullname=f'{get_random_string()} {get_random_string()}',
             age=random.randint(5, 100),
             nickname=get_random_string(len=10)))


session.commit()


all_users_ids = [u[0] for u in session.query(User.id).all()]
for i in range(300):
    session.add(Email(email_address=f'{get_random_string()}@{get_random_string()}.com',
                      user_id=random.choice(all_users_ids)))


session.commit()
