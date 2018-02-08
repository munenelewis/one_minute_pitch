from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    #users = db.relationship('User',backref = 'pitches',lazy="dynamic")
    
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
  

    def __repr__(self):
        return f'User {self.username}'
# class Category(db.Model):
#     __tablename__='categories'
#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     @classmethod
#     def get_categories(cls):
#         categories = Category.query.all()

#         return categories


class Pitch(db.Model):
    __tablename_='pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    body = db.Column(db.String())
    #user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    # comments = db.Column(db.String())

    def save_pitches(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls):
        pitches = pitches.query.all()
        return pitches

    @classmethod
    def get_categories(cls, category):
        pitch_cat = pitches.query.filter_by(category=category)
        return pitch_cat

    def __init__(self,title, body, category):
        self.title= title
        self.body= body
        self.category= category


