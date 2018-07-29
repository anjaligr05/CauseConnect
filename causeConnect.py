from flask import Flask, render_template, session, request, abort, flash, redirect, url_for
app = Flask(__name__)
import os

@app.route('/')
def home():
	author = "me"
	name = "You"
	if not session.get('logged_in'):
		return render_template('login.html', author = author, name=name)
	else:
		return 'Hello There'

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
    	if request.form['password'] == 'password' and request.form['username'] == 'admin':
        	session['logged_in'] = True
		return redirect(url_for('choose'))
    else:
        flash('wrong password!')
    return home()

@app.route('/SignUp', methods=['GET', 'POST'])
def signUp():
	print 'in here'
	print request.form
	return render_template('SignUp.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
	
if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.debug = True
	app.run('0.0.0.0', 12345)
