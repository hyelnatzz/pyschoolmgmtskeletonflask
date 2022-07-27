from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Student(db.Model, UserMixin):
    """Model for student accounts."""

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(20),
                    nullable=False,
                    unique=True)
    full_name = db.Column(db.String(100),
                    nullable=False,
                    unique=False)
    email = db.Column(db.String(40),
                    unique=True,
                    nullable=False)
    password = db.Column(db.String(200),
                    unique=False,
                    nullable=False)
    dob = db.Column(db.String(15),
                    nullable=False,
                    unique=False)
    address = db.Column(db.String,
                    nullable=False,
                    unique=False)


    def __repr__(self):
        return '<User {}>'.format(self.username)
