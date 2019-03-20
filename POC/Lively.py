
# coding: utf-8

# In[5]:


from flask import Flask, flash, render_template, request, redirect, session, url_for
from flask_wtf import Form
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
import hashlib
import locale
import pymysql
import time


# In[6]:


app = Flask(__name__)
app.config['SECRET_KEY'] = '8ffe05624dfe0efdf7c7f67288d4f4ce5005e0dfb6a1bc48366ef9906dd0586e'
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8') # To get money formatting


# In[7]:

#####################################################################
#                         INDEX/HOME                                #
#####################################################################

# Visit site for first time. Pictures.
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

# Home page. Displays admin interface if user is admin.
@app.route('/home')
def home():

	# Disallow unlogged in users from requesting homepage.
	if 'username' not in session or session['username'] is '':
		return redirect(url_for('index'))

	return create_trip(no_error=True)

#####################################################################
#                          ADMIN PANEL                              #
#####################################################################

# Delete user from admin panel
@app.route('/delete-user/<username>')
def delete_user(username):

	cursor = db.cursor()
	cursor.execute("delete from user where username='" + username + "';")
	db.commit()

	return redirect(url_for('home'))

# Suspend user from admin panel
@app.route('/suspend-user/<username>')
def suspend_user(username):

	cursor = db.cursor()
	cursor.execute("select suspended from user where username='" + username + "';")
	if cursor.fetchall()[0][0] == 1:
		cursor.execute("update user set suspended=0 where username='" + username + "';")
	else:
		cursor.execute("update user set suspended=1 where username='" + username + "';")
	db.commit()

	return redirect(url_for('home'))

# Make user an Admin from admin panel
@app.route('/make-admin/<username>')
def make_admin(username):

	cursor = db.cursor()
	cursor.execute("update user set is_admin=1 where username='" + username + "';")
	db.commit()

	return redirect(url_for('home'))

#####################################################################
#                        LOGIN / REGISTRATION                       #
#####################################################################

# Login/Registration Page. Redirects to home if already logged in.
@app.route('/login-page')
def login_page():

	# Show login page if not logged in. Redirect to home if already logged in.
	if 'username' not in session or session['username'] == '':
		return render_template('login.html')
	else:
		return redirect(url_for('home'))

# On Login Form Submit. Loads home page or shows error.
@app.route('/login', methods=['POST'])
def verify_credentials():

	# Parse user input fields
	name=request.form['login_username']
	password=hashlib.sha256(request.form['login_password'].encode('utf-8')).hexdigest()

	# Query Database
	cursor = db.cursor()
	cursor.execute("select * from user where username = '" + name + "' and password = '" + password + "';")
	rows = cursor.fetchall()
	error = None

	if rows:
		# User found
		if rows[0][7] != 1:
			# Not suspended
			session['username'] = rows[0][0]
			session['email'] = rows[0][2]
			session['is_admin'] = rows[0][3]
			session['name'] = rows[0][4]

			# # Set current trip id for this user.
			# query = get_current_trip_id()
			# cursor.execute(query)
			# trip_ids = cursor.fetchall()

			# if len(trip_ids) > 0:
			# 	# There are trips for this user. If no, just make it when they start adding attractions.
			# 	session['current_trip_id'] = trip_ids[0][0]

			# return redirect(url_for('home'))
		else:
			# Suspended user
			error='User suspended.'
	else:
		# No such user. Login again.
		error = 'Incorrect username or password. Please try again.'
	return render_template('login.html', error=error)

# Logs out of system and redirects to pictures.
@app.route('/logout')
def logout():

	# Clear out session variables
	session.clear()
	return redirect(url_for('index'))

# On Register Form Submit. Loads home page.
# TODO: Re-fill out correct fields when registration fails.
@app.route('/register', methods=['POST'])
def register():

	# Parse user input fields
	name=request.form['register_username']
	password1=hashlib.sha256(request.form['register_password'].encode('utf-8')).hexdigest()
	password2=hashlib.sha256(request.form['register_password2'].encode('utf-8')).hexdigest()
	firstname=request.form['register_firstname']
	lastname=request.form['register_lastname']
	email=request.form['register_email']
	age=request.form['register_age']
	street=request.form['register_streetaddress']
	city=request.form['register_city']
	state=request.form['register_state']
	country=request.form['register_country']
	zipcode=request.form['register_zip']

	# Check if all user fields filled in
	if name == '' or password1 == '' or password2 == '' or firstname == '' or firstname == '' or lastname == '' or email == '' or age == '' or street == '' or city == '' or state == '' or country == '' or zipcode == '':
		error = 'Please fill out all the fields.'
		return render_template('login.html', error2=error, scroll="register")

	# Check that passwords match
	if password1 != password2:
		error = 'Passwords do not match.'
		return render_template('login.html', error2=error, scroll="register")

	# Parse street_no from street
	street_no = -1

	

	street_no = str(street.split(" ")[0])
	street = street[street.index(" ") + 1:]

	# Write to Database
	cursor = db.cursor()
	cursor.execute("insert into Address (street_no, street_name, city, state, country, zip) values ("
			+ street_no + ", '" + street + "', '" + city + "', '" + state + "', '" + country + "', '" + zipcode + "');")

	cursor.execute("insert into User (username, password, email, is_admin, first_name, last_name, address_id,age,suspended) values ('"
	+ name + "', '" + password1 + "', '" + email + "', false, '" + firstname + "', '" + lastname + "', (select max(address_id) from address),'" + age + "', 0);")
	db.commit()

	# Update current user session
	session['username'] = name
	session['name'] = firstname
	session['is_admin'] = 0
	session['email'] = email

	return redirect(url_for('home'))

def create_trip(no_error):

	# Query database when user is admin for admin panel
	if session['is_admin']:

		# Get user table information.
		cursor = db.cursor()
		cursor.execute("select * from user;")
		users = [dict(is_admin="Yes" if row[3] == 1 else "No", username=row[0], password=row[1], first_name=row[4], last_name=row[5], email=row[2], suspended="Yes" if row[7] == 1 else "No") for row in cursor.fetchall()]

		# Get attraction table information.
		attractions = get_attractions_data()

		if no_error:
			return render_template("home.html", session=session, users=users, attractions=attractions, no_trip="Here, you can start making your first trip!")
		else:
			return render_template("home.html", session=session, users=users, attractions=attractions, no_trip_error="You must first create a new trip!")

	# Not an admin
	if no_error:
		if 'current_trip_id' not in session or not session['current_trip_id']:
			return render_template("home.html", session=session, no_trip="Here, you can start making a new trip!")
		return render_template("home.html", session=session)
	else:
		return render_template("home.html", session=session, no_trip_error="You must first create a new trip!")

# In[8]:


if __name__ == '__main__':

	# Note: If your database uses a different password, enter it here.
	db_pass = 'messi@123'

	# Make sure your database is started before running run.py
	db_name = 'team_lively1'
	db = pymysql.connect(host='127.0.0.1', user='root', passwd=db_pass, db=db_name)
	app.run(debug=True)
	db.close()

