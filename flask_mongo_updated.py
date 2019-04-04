#! /anaconda3/bin/python

from flask import Flask, render_template, url_for, request, session, redirect
import logging
from logging.handlers import RotatingFileHandler
import requests

from pymongo import MongoClient

app = Flask(__name__)
 # instantiate the db connection


@app.route('/')
def welcome():
	app.logger.info("Successfully invoked the index route")
	return "Welcome to Adaptive Itinerarizer"
	
	
@app.route('/add/<string:username>//<string:tag1>/<string:tag2>/<string:tag3>', methods=['GET'])
def add(username, tag1, tag2, tag3):

	user = db.users0
	users = user.insert(
		{
			'username': username,
			'tag1': tag1,
			'tag2': tag2,
			'tag3': tag3,
			
		}
	)
	return render_template('login.html', username=username, tag1=tag1, tag2=tag2, tag3=tag3)


@app.route('/attractions/<string:tag1>', methods=['GET'])
def attractions(tag1):
	attractions = db.attractions
	for entry in attractions.find({"Tag(s)":tag1}):
		lat = entry["Latitude"]
		lan = entry["Longitude"]
		des = str(lat)+','+str(lan)
		org = ''
		API_KEY = 'AIzaSyB2NHLaqVDF0uSmuNBMXI3DVsUanzdRD7Q'
		url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+org+'&destination='+des+'&key='+API_KEY
		route = requests.get(url)
	#return render_template('login.html')

@app.route('/fetch')
def fetch():
	user_collection = db["users"]
	for aUser in user_collection.find({"userId":9145}):
		app.logger.info(aUser['categories'])
		
		return render_template('welcome.html',name=aUser['name'],age=aUser['age'],result=dict(aUser['categories']))

@app.route('/fetch/<user_id>')
def register(user_id):
	print(type(user_id))
	print(db.list_collection_names())
	user_collection = db["users"]
	app.logger.info(user_collection.find_one({"userId":int(user_id)}))
	aUser=user_collection.find_one({"userId":int(user_id)})
	app.logger.info(aUser)
	if(aUser):
		#app.logger.info()
		return render_template('welcome.html',name=aUser['name'],age=aUser['age'],result=dict(aUser['categories']))
	else:
		app.logger.error('No user found')
		return "User not found"

if __name__ == '__main__':
	app.secret_key = '______________'

	# Make sure your database is started before running run.py
	db_name = 'adaptive'
	client = MongoClient('localhost', 27017)
	db = client[db_name]
	
	handler = RotatingFileHandler('dummy.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	logging.getLogger(__name__).setLevel(logging.INFO)
	logging.getLogger(__name__).addHandler(handler)
	app.logger.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	app.run(debug=True)