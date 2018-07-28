import os,sys,random, datetime
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify, session, Markup, send_from_directory

app = Flask(__name__)

app.secret_key = "secret_key"

#show basic navigation 

@app.route('/')

def index():

    return render_template('index.html')


#Route for signing up a user

@app.route('/signup/', methods=["GET", "POST"])

def signup():

    if request.method == "GET":

        return render_template('signup.html')

    else:    

        try:

            '''#get user registration info'''

            dsn = functions.get_dsn()

            conn = functions.getConn(dsn)
            email = request.form['email']

            password1 = request.form['password1']

            password2 = request.form['password2']

            bid = request.form['bid']

            classyear = request.form['classyear']
            if password1 != password2:

                flash('The passwords you entered do not match.')

                return redirect( url_for('signup'))

            hashed = hash(password1.encode('utf-8'), bcrypt.gensalt())

            row = functions.emailexists(conn, email)

            if row is not None: 

                flash('That user is already taken. Please choose a different one.')

                return redirect( url_for('signup') )

            else:

                #signup successful, add information to table

                functions.insertinfo(conn, email, password1, bid, classyear)

                functions.inserthashed(conn, bid, hashed)

                

                #session will be updated in the later version 

                session['email'] = email

                session['logged_in'] = True

                session['BID'] = bid

                

                #lead user back to home page or to search page

                return redirect(url_for('insert',email=email))        

            

        except Exception as err:

             flash('form submission error '+str(err))

             return redirect( url_for('signup') )

