from . import main
from flask import render_template,request


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    return render_template('index.html',title=title)
@main.route('/login')
def login():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    return render_template('login.html',title=title)
