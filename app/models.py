from . import db

class Pitch:
    def __init__(self,pitch):
        self.pitch = pitch
    
class Category:
     __tablename__='users'
     pickup = db.Column(db.String(255))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))


    def __repr__(self):
        return f'User {self.username}'

class Submission(db.Model):
    __tablename__ = 'Submission'
    id = db.Column(db.Integer,primary_key = True)
    details = db.Column(db.String(255))

class Profile(db.Model):
    __tablename__ = 'Profile'
    id = db.Column(db.Integer,primary_key = True)
    details = db.Column(db.String(255))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    def __repr__(self):
        return f'User {self.name}'