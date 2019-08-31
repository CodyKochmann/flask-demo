# -*- coding: utf-8 -*-

'''
This series of problems or questions relate to a position (contract or permanent hire negotiable) for a backend developer specializing in the use flask, sqlalchemy, redis, docker, unit testing, and git.  We are looking for someone whose work can be released to production soon after hiring, though there's always room for learning on the job.  Wherever possible, do your first draft on this form so we can see your thought process as well as your final result.

- Second (Starting Up); Using python 3+, and flask, please create a small and functioning flask application.
-- Add a dict of any give cities of your choosing as the keys and an attraction in that city as the value
-- Create a GET endpoint /city/*city*/attraction/ that will reply with the attraction in JSON format
-- or an appropriate error if the city is not found

~~ show us the code you wrote (preferably written here)

(none of the following are necessary bout would be impressive)
!! extra credit if you provide us a with a github or gitlab link to your work (as an alternative to writing it here)
!! extra credit if you show us that you used docker in getting this application running
'''

'''
This series of problems or questions relate to a position (contract or permanent hire negotiable) for a backend developer specializing in the use flask, sqlalchemy, redis, docker, unit testing, and git.  We are looking for someone whose work can be released to production soon after hiring, though there's always room for learning on the job.  Wherever possible, do your first draft on this form so we can see your thought process as well as your final result.

- Third (Models); Using sqlalchemy, refactor your previous application to move the city-and-attraction data to a local database (mysql, sqlite, or similar)
-- Create a table and model for cities and attractions
-- Add your previous five cities to this new database
-- Modify the GET endpoint to pull from when responding to /city/*city*/attraction/
-- Add a POST endpoint to add a new city and attraction to the database

~~ show us the code changes you made (preferably written here)
~~ show us a curl statement used to add a sixth city
~~ show us a table dump of the table after the sixth has been added

(none of the following are necessary bout would be impressive)
!! extra credit if you provide us a with a github or gitlab link to your work (as an alternative to writing it here)
!! extra credit if you normalize the database relationship between cities and attractions both at the database and at the model layer
!! extra credit if you add try+except clauses to safeguard your data
!! extra credit if you show us that you added your database via docker/kubernetes
'''

import logging, os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from attractions import city_map, load_db, DBTypes


DB_PATH = '/db/test.db'


app = Flask(__name__)
db = load_db(
    app=app,
    uri='sqlite:////db/test.db',
    populate=(not os.path.exists(DB_PATH))
)


# set log level
app.logger.setLevel(logging.DEBUG)  # I like my logs

def get_attraction(city):
    print('get attraction recieved', city)
    result = DBTypes.Attraction.query.filter_by(city=city).first()
    return {'error': 'unregistered city: {}'.format(city)} if result is None else result.name

def post_attraction(city, name):
    print('post attraction recieved', city)
    try:
        db.add_attraction(city, name)
        return 'success'
    except Exception as ex:
        logging.exception(ex)
        return {'error': 'couldnt process: {}, {}'.format(city, name)}

@app.route('/city/<city>/attraction/', methods=['GET', 'POST'])
def attraction(city):
    if request.method == 'GET':
        return get_attraction(city)
    elif request.method == 'POST' and 'name' in request.args:
        return post_attraction(city, request.args['name'])

@app.route('/')
def index():
    return 'good to go'
