
import os
from unittest import TestCase
from sqlalchemy import exc


from models import db, User
from app import app

os.environ['DATABASE_URI'] = 'postgresql:///news-app-test'
app.config['SQLALCHEMY_ECHO'] = True

db.create_all()


class UserModelTest(TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

        user1 = User.register("test1", "test",
                              "test", "01/01/1989", "test@test.com", '123456789')

        db.session.add(user1)
        db.session.commit()

        user1 = User.query.get("test")

        self.user1 = user1

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    # User Registering Testing
#    Valid Input

    def test_valid_register(self):
        user1_test = User.register("test1", "test_first",
                                   "test_last", "01/01/1989", "test@test.com", '123456789')

        db.session.commit()

        user1_test = User.query.get("test1")
        self.assertIsNotNone(user1_test)
        self.assertEqual(user1_test.username, "test1")
        self.assertEqual(user1_test.email, "test@test.com")
        self.assertNotEqual(user1_test.password, '123456789')
        # Bcrypt strings should start with $2b$
        self.assertTrue(user1_test.password.startswith("$2b$"))

    # Invalid Username
    def test_invalid_username_register(self):
        no_user = User.register(None, "test_first",
                                "test_last", "01/01/1989", "test@test.com", '123456789')

        no_user.username = "test1"
        with self.assertRaises(exc.IntegrityError) as context:
            db.session.add(no_user)
            db.session.commit()

    # Invalid email
    def test_invalid_email_register(self):
        no_email = User.register("test1", "test_first",
                                 "test_last", "01/01/1989", None, '123456789')

        no_email.username = "test1"
        with self.assertRaises(exc.IntegrityError) as context:
            db.session.add(no_email)
            db.session.commit()
