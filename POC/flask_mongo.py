from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from classes import *
from pymongo import MongoClient

import bcrypt
import time

app = Flask(__name__)
app.config['MONGO_DBNAME'] = '____________'
app.config['MONGO_URI'] = '____________'

mongo = PyMongo(app) # instantiate the db connection


@app.route('/add/<string:username>//<string:tag1>/<string:tag2>/<string:tag3>', methods=['GET'])
def add(username, tag1, tag2, tag3):
    
        user = mongo.db.users0
        users = user.insert(
            {
                'username': username,
                'tag1': tag1,
                'tag2': tag2,
                'tag3': tag3,
                
            }
        )
        return render_template('login.html', username=username, tag1=tag1, tag2=tag2, tag3=tag3)

   

if __name__ == '__main__':
    app.secret_key = '______________'
    app.run(debug=True)