from app import app

from flask import render_template, request
from flask_wtf import Form
from wtforms import TextField
from sqlalchemy import and_, desc
import sqlsoup

db = sqlsoup.SQLSoup('mssql+pyodbc://ds01/USW2')


class SearchForm(Form):
    srch_last = TextField('srch_last')


@app.route('/members', methods=['GET', 'POST'])
def members():
    form = SearchForm()

    members = []

    if form.is_submitted():
        last = form.srch_last.data
        where = (db.member.LastName == last)
        members = db.member.filter(where).limit(10).all()

    return render_template('members.html',
                           members=members,
                           form=form)