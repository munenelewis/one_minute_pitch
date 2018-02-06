from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class Pitch:
    def __init__(self,pitch):
        self.pitch = pitch
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'
class Category(db.Model):
    __tablename_='categories'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    @classmethod
    def get_categories(cls):
        categories = Category.query.all()

        return categories