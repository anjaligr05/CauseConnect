from flask import Flask, render_template, session, request, abort, flash, redirect
app = Flask(__name__)
import os

@app.route('/')
def home():
	author = "me"
	name = "You"
	if not session.get('logged_in'):
		return render_template('login.html', author = author, name=name)
	else:
		return "Hello there!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
	
if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.debug = True
	app.run('0.0.0.0', 12345)
