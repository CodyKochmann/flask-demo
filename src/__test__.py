# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep
import unittest, os, socket, json

import requests

from attractions import city_map

# ugly incantation just to get server running in background
# ideally you would want this to re-spin up in on every setUp()
def run_flask():
    for line in os.popen('/flaskvenv/bin/flask run'):
        print('server -', line.strip())
Thread(target=run_flask, daemon=True).start()
sleep(3)


class AttractionsTest(unittest.TestCase):
    def setUp(self):
        print('setting up')

    def tearDown(self):
        print('tearing down')

    def test_server_listening(self):
        ''' tests if the server is actually listening '''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('127.0.0.1', 5000))
            s.send(b'')
        finally:
            s.close()

    def test_get_city(self):
        ''' positive testing of the server '''
        for cityname, attraction in city_map.items():
            print('testing:', cityname, '->', attraction)
            response = requests.get('http://0:5000/city/{}/attraction/'.format(cityname)).text
            self.assertEqual(attraction, response)

    def test_missing_city(self):
        ''' negative testing of the server '''
        # this would be a great place to fuzz ;)
        print('testing to see if america returns a city attraction')
        response = requests.get('http://0:5000/city/america/attraction/').text
        self.assertEqual(json.loads(response), {"error": "unregistered city: america"})

if __name__ == '__main__':
    unittest.main(verbosity=2)
