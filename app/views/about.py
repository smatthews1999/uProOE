from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/members', methods=['GET', 'POST'])
def members():

    members = []

    return render_template('members.html',
                           members=members)
