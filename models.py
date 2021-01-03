from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from datetime import datetime

from app.extensions import db
from app.extensions import login

@login.user_loader
def load_user(id):
    #query database for id from User class
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class City(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(4))
    name = db.Column(db.String(50))        

##ELDER MODEL-python converts into SQL
class Friends(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
#Create a function to make string when add something
    def __repr__(self):
        return '<Name %r>' % self.id    

class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pattern = db.Column(db.String(64), index=True, unique=True)

if __name__ == '__main__':
    db.create_all()

