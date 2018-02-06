from . import main
from flask import render_template,request
from flask_login import login_required
from flask_login import login_required
from ..models import Category


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    categories = Category.get_categories()
    return render_template('index.html',title=title,categories=categories)
