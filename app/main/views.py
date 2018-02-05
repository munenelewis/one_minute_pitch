from . import main
from flask import render_template,request
from flask_login import login_required
from flask_login import login_required


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    return render_template('index.html',title=title)
# @main.route('/login')
# def login():
#     '''
#     View root page function that returns the index page and its data
#     '''
#     title = 'Home - Welcome to The best Pitching Website Online'

#     return render_template('login.html',title=title)

@main.route('/interview')
def interview():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    return render_template('interview.html',title=title)

@main.route('/pickup')
def pickup():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    return render_template('pickup.html')

@main.route('/promo')
def promo():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    return render_template('promotionpitch.html')

@main.route('/product')
def product():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    return render_template('product.html')

@main.route('/coment')
@login_required
def coment():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    return render_template('comments.html')
