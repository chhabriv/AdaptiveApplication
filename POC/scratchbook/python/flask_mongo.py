from flask import Flask, render_template, url_for, request, session, redirect,jsonify
import logging
from logging.handlers import RotatingFileHandler
import user_crud
from mongoconnection import MongoConnection
from pymongo import MongoClient
from flask_pymongo import PyMongo
import service
import json

app = Flask(__name__)
#app.config['MONGO_URI'] = "mongodb://localhost:27017/adaptive"
#mongo = PyMongo(app)
 # instantiate the db connection


@app.route('/')
def welcome():
	app.logger.info("Successfully invoked the index route")
	return "Welcome to Adaptive Itinerarizer"
	
	
@app.route('/fetch/user/<user_id>')
def fetchUsers(user_id):
	return user_crud.fetchUser(user_id)
	

@app.route('/suggest', methods=['POST'])
def suggest_places():
    app.logger.info(request.is_json)
    input_data = request.get_json()
    user_id,places = service.plan_trip(json.dumps(input_data))
    app.logger.info(user_id)
    app.logger.info(places)
    return jsonify(user_id=user_id,places=str(places))
    #print(input_data)
    #return str(input_data)
        
    

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
	#db_name = 'adaptive'
	#client = MongoClient('localhost', 27017)
	#db = client[db_name]
	#conn = MongoConnection()
	#MongoConnection._init_(app)
	handler = RotatingFileHandler('dummy.log', maxBytes=10000, backupCount=1)
	#handler.setLevel(logging.INFO)
	logging.getLogger(__name__).setLevel(logging.INFO)
	logging.getLogger(__name__).addHandler(handler)
	app.logger.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	app.run(debug=True)