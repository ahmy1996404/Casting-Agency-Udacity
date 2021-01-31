import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

#
# database_name = "casting_agency"
# database_path = "postgres://{}/{}"\
#     .format('postgres:root@localhost:5432', database_name)
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

    '''
    Movies

    '''


movies_actors = db.Table('movies_actors',
                         db.Column('movie_id', db.Integer,
                                   db.ForeignKey('movies.id'),
                                   primary_key=True),
                         db.Column('actor_id', db.Integer,
                                   db.ForeignKey('actors.id'),
                                   primary_key=True))

'''
Movies

'''


class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)
    actors = db.relationship('Actors',
                             secondary=movies_actors,
                             backref=db.backref('movies',
                                                lazy=True))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        formated_actor = []
        for actor in self.actors:
            formated_actor.append({'id': actor.id, 'name': actor.name})
        # print(formated_actor)
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': formated_actor
        }


'''
Actors

'''


class Actors(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        formated_movies = []
        for movie in self.movies:
            formated_movies.append({'id': movie.id, 'title': movie.title})
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies': formated_movies

        }
