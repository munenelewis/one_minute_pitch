from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from .forms import ReviewForm,UpdateProfile

from ..models import Pitch
from .. import db


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    pitches = Pitch.query.filter_by(category='biz').all()
    print(pitches)

    return render_template('index.html',title=title,pitches=pitches)
@main.route('/comment', methods = ['GET','POST'])
@login_required
def comment():

  return  render_template ('coment.html')

@main.route('/user/<uname>')
@login_required

def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
          
          
          user.bio = form.bio.data

          db.session.add(user)
          db.session.commit()

          return redirect(url_for('.profile',uname=user.username))

    return render_template("profile/profile.html", user = user)
