from flask import Flask, render_template, session, request, abort, flash, redirect, url_for
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)
import os

@app.route('/')
def home():
	author = "me"
	name = "You"
	return render_template('login.html', author = author, name=name)

@app.route('/hero', methods=['GET','POST'])
def choose():
	if request.method == "GET":
		return render_template('hero.html')
	else:
		if 'donater' in request.form :
			'''redirect to post donation'''
			return "Thank you for donation"
		elif 'nonProfiter' in request.form:
			return "Requesting a donation"

@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    if 'signUp' in request.form:
	return redirect(url_for('signUp'))
    elif 'login' in request.form:
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])
	Session = sessionmaker(bind=engine)
    	s = Session()
    	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    	result = query.first()
    	if result:
		return redirect(url_for('choose'))
    	else:
        	flash('wrong password!')
    return home()

@app.route('/SignUp', methods=['GET', 'POST'])
def signUp():
	return render_template('SignUp.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
	
if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.debug = True
	app.run('0.0.0.0', 12345)
