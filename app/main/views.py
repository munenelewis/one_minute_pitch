from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from .forms import ReviewForm,UpdateProfile,PitchForm,CommentsForm,UpvoteForm

from ..models import Pitch,Comment,User
from .. import db


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    bussines = Pitch.query.filter_by(category='bussines').all()
    print(bussines)
    pick_up = Pitch.query.filter_by(category='pick_up').all()
    interview = Pitch.query.filter_by(category='interview').all()

    product = Pitch.query.filter_by(category='product').all()

    return render_template('index.html',title=title,bussines=bussines,product=product,interview=interview,pick_up=pick_up)
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
@main.route('/newpitch' ,methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        pitches = Pitch(title = form.title.data,body = form.body.data,category = form.category.data)

        pitches.save_pitches()
        # print('Your Pitch has been succenssfully saved!')
        return redirect(url_for('main.new_pitch'))
    return render_template('newpitch.html',pitch_form = form)


@main.route('/bussines')

def bussines():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    pitches = Pitch.query.filter_by(category='bussines').all()
    print(pitches)

    return render_template('bussines.html',title=title,pitches=pitches)

@main.route('/product')

def product():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    pitches = Pitch.query.filter_by(category='product').all()
    print(pitches)

    return render_template('product.html',title=title,pitches=pitches)

@main.route('/interview')

def interview():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    pitches = Pitch.query.filter_by(category='interview').all()
    print(pitches)

    return render_template('interview.html',title=title,pitches=pitches)

@main.route('/pick_up')

def pick_up():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    pitches = Pitch.query.filter_by(category='pick_up').all()
    print(pitches)

    return render_template('pick_up.html',title=title,pitches=pitches)


@main.route('/pitch/comments/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    vote_form = UpvoteForm()
    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data,username=current_user.username,votes=form.vote.data)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    #title = f'{pitch_result.id} review'
    return render_template('new_comment.html',comment_form=form, vote_form= vote_form)
