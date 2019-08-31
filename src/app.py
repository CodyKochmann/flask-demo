# -*- coding: utf-8 -*-

'''
This series of problems or questions relate to a position (contract or permanent hire negotiable) for a backend developer specializing in the use flask, sqlalchemy, redis, docker, unit testing, and git.  We are looking for someone whose work can be released to production soon after hiring, though there's always room for learning on the job.  Wherever possible, do your first draft on this form so we can see your thought process as well as your final result.

- Second (Starting Up); Using python 3+, and flask, please create a small and functioning flask application.
-- Add a dict of any give cities of your choosing as the keys and an attraction in that city as the value
-- Create a GET endpoint /city/*cityname*/attraction/ that will reply with the attraction in JSON format
-- or an appropriate error if the cityname is not found

~~ show us the code you wrote (preferably written here)

(none of the following are necessary bout would be impressive)
!! extra credit if you provide us a with a github or gitlab link to your work (as an alternative to writing it here)
!! extra credit if you show us that you used docker in getting this application running
'''

from flask import Flask
from attractions import city_map

# import sanity check
assert isinstance(city_map, dict), 'city_map should have been a dict... {}'.format(city_map)

app = Flask(__name__)

@app.route('/')
def index():
    return 'good to go'
