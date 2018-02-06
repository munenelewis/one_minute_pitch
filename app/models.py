from . import db



class Pitch:
    def __init__(self,pitch):
        self.pitch = pitch
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    


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