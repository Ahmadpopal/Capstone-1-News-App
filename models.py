from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):

    __tablename__ = "users"

    def __repr__(self):
        return f"<USER Username:{self.username},  Email{self.email}>"

    username = db.Column(db.Text, primary_key=True,
                         unique=True, nullable=False)
    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=False)
    dateofbirth = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    @classmethod
    def register(cls, username, firstname, lastname, dateofbirth, email, password):
        """ Register User with hashed password and return user"""
        hashed = bcrypt.generate_password_hash(password)

        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, firstname=firstname, lastname=lastname, dateofbirth=dateofbirth, email=email, password=hashed_utf8)

    @classmethod
    def authenticate(cls, username, password):
        """Validate if user and password correct if not return false"""

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, password):

            return u
        else:
            return False


def connect_db(app):
    db.app = app
    db.init_app(app)
