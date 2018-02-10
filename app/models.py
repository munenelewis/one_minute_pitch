from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func


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
    #pitch = db.relationship("Pitch", backref="users", lazy = "dynamic")
    #comment = db.relationship("Comments", backref="users", lazy = "dynamic")
    vote = db.relationship("Votes", backref="users", lazy = "dynamic")
    pitches = db.relationship('Pitch',backref = 'users',lazy="dynamic")
    comment = db.relationship("Comment", backref="users", lazy = "dynamic")

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
class Category(db.Model):
     # table columns
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    # save pitches
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories


class Pitch(db.Model):
    __tablename_='pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    body = db.Column(db.String())
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
    vote = db.relationship("Votes", backref="pitch", lazy = "dynamic")



    # comments = db.Column(db.String())

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls):
        pitches = pitch.query.all()
        return pitches
    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitch.clear()
    def get_pitches(id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches





class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitch.id"))

    

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comment = Comment.query.order_by(Comment.time_posted.desc()).filter_by(pitches_id=id).all()
        return comment

#votes
class Votes(db.Model):
    '''class to model votes '''
    __tablename__='votes'

    id = db.Column(db. Integer, primary_key=True)
    vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitch.id"))

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,user_id,pitches_id):
        votes = Vote.query.filter_by(user_id=user_id, pitches_id=pitches_id).all()
        return votes

