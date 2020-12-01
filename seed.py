"""Seed file to make simple data"python"""

from models import db, User
from app import app

# Create all tables
db.drop_all()
db. create_all()


u1 = User(username="ahmad", firstname="ahmad imran", lastname="popal",
          dateofbirth="05/03/1989", email="imranpopal@yahoo.com", password="1234")


db.session.add(u1)

db.session.commit()
