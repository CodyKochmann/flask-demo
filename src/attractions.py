# -*- coding: utf-8 -*-

import os

from flask_sqlalchemy import SQLAlchemy

city_map = {
    "baltimore": "national aquarium",
    "severn": "nsa headquarters",
    "san francisco": "golden gate bridge",
    "rachel": "area 51",
    "new york": "lady liberty"
}


def load_db(*, app, uri, populate):

    app.config['SQLALCHEMY_DATABASE_URI'] = uri

    db = SQLAlchemy(app)

    class Attraction(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        city = db.Column(db.String(64), unique=True, nullable=False)
        name = db.Column(db.String(128), nullable=False)
        def __repr__(self):
            return str({'city':self.city, 'name':self.name})

    db.create_all()

    if populate:
        for city, name in city_map.items():
            db.session.add(Attraction(city=name, name=name))

        db.session.commit()

    return db
