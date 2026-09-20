from random import choice as rc

from faker import Faker

from app import create_app
from models import Message
from app.db import db

fake = Faker()

usernames = [fake.first_name() for i in range(10)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():

    Message.query.delete()
    
    messages = []

    for i in range(20):
        message = Message(
            body=fake.sentence(),
            username=rc(usernames),
        )
        messages.append(message)

    db.session.add_all(messages)
    db.session.commit()        

app=create_app()
if __name__ == '__main__':
    with app.app_context():
        make_messages()