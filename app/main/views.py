from flask import render_template, request, redirect, url_for, abort,flash
from ..requests import get_blogQuotes
from . import main
from ..models import User
from flask_login import login_required, current_user
from datetime import datetime
from .. import db
from .forms import UpdateProfile

@main.route('/')
def index():
    '''
    '''
    blogQuote =get_blogQuotes()
    title = 'Welcome to My Blog'
    return render_template('index.html',title = title, blogQuote=blogQuote)

@main.route('/home')
@login_required
def home():
    return render_template("home.html" )

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    