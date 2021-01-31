import os
from flask import Flask, request, abort, jsonify
from models import setup_db, Movies, Actors, movies_actors
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import requires_auth, AuthError
import random

PAGINATION_PER_PAGE = 10


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PATCH, POST, DELETE, OPTIONS'),
        response.headers.add('Access-Control-Allow-Origin', '*'),

        response.headers.add('Access-Control-Allow-Domain', '*')
        return response

    @app.route('/')
    def get_greeting():
        return "hello"

    '''
    Create an endpoint to handle GET requests
    for all available Movies.
    '''
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(jwt):
        # get all movies
        # make the pagination for every 10 movies)
        # the number of movies variable 'PAGINATION_PER_PAGE'
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * PAGINATION_PER_PAGE
        end = start + PAGINATION_PER_PAGE
        # get all movies
        movies = Movies.query.all()
        # format the movies
        formated_movies = [movie.format() for movie in movies]
        # return a Response with the JSON representation
        # 'sucsses' , 'movies' , 'total_movie' ,
        return jsonify({
            'success': True,
            'movies': formated_movies[start:end],
            'total_movies': len(formated_movies)
        })
    '''
      Create an endpoint to POST a new move.
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth('add:movies')
    def add_movies(jwt):
        # get the post request data  'title' , 'release_date'
        body = request.get_json()
        # if empty
        if ((body.get('title') == "") or
                (body.get('release_date') == "")):
            abort(422)
        try:
            # create move
            move = Movies(title=body.get('title', None),
                          release_date=body.get('release_date', None))
            move.insert()
            # return a Response with the JSON representation
            # 'sucsses' , 'create'
            return jsonify({
                'success': True,
                'create': move.id
            })
        except ex:
            print(ex)
            abort(422)
    '''
    Create an endpoint to DELETE movie using a movie ID.
    '''
    @app.route('/movies/<movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(jwt, movie_id):
        # get movie that matches with movie_id
        movie = Movies.query.get(movie_id)
        # if there isnot such id with this id
        if movie is None:
            abort(422)
        # if exist
        else:
            # delete this movie
            movie.delete()
            # return a Response with the JSON representation
            # 'sucsses' , 'delete'
            return jsonify({
                'success': True,
                'delete': movie_id
            })

    '''
      Create an endpoint to update movie using a movie ID.
    '''
    @app.route('/movies/<movie_id>', methods=['PATCH'])
    @requires_auth('update:movie')
    def update_movie(jwt, movie_id):
        # get movie that matches with movie_id
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        # get the post request data  'title' , 'release_date'
        body = request.get_json()

        try:
            # update move
            if 'title' in body:
                movie.title = body.get('title', None)
            if 'release_date' in body:
                movie.release_date = body.get('release_date', None)
                movie.update()
                # return a Response with the JSON representation
                # 'sucsses' , 'update'
                return jsonify({
                    'success': True,
                    'update': movie_id
                })

        except ex:
            print(ex)
            abort(422)

    '''
     Create a GET endpoint to get actors based on move.
    '''
    @app.route('/actors/<move_id>/movies')
    @requires_auth('get:movies_by_actor')
    def get_movies_by_actor(jwt, move_id):
        # get the  actors filtered by move
        actors = Actors.query.filter(Actors.movies.any(id=move_id)).all()
        if len(actors) == 0:
            abort(404)
        # make the pagination for every 10 movies)
        # the value of 'PAGINATION_PER_PAGE' variable
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * PAGINATION_PER_PAGE
        end = start + PAGINATION_PER_PAGE
        # # format the actors
        formated_actor = [actor.format() for actor in actors]
        # return a Response with the JSON representation
        # 'sucsses' , 'actors' , 'total_actors' ,
        return jsonify({
            'success': True,
            'actors': formated_actor[start:end],
            'total_actors': len(actors),
        })

    '''
      Create an endpoint to handle GET requests
      for all available actors.
    '''
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(jwt):
        # get all actors
        # make the pagination for every 10 movies)
        # the number of movies variable 'PAGINATION_PER_PAGE'
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * PAGINATION_PER_PAGE
        end = start + PAGINATION_PER_PAGE
        # get all actors
        actors = Actors.query.all()
        # format the actors
        formated_actors = [actor.format() for actor in actors]

        # return a Response with the JSON representation
        # 'sucsses' , 'movies' , 'total_movie' ,
        return jsonify({
            'success': True,
            'actors': formated_actors[start:end],
            'total_actors': len(formated_actors),
        })

    '''
       Create an endpoint to POST a new actor.
    '''

    @app.route('/actors', methods=['POST'])
    @requires_auth('add:actor')
    def add_actors(jwt):
        # get the post request data  'name' , 'age' , 'gender'
        body = request.get_json()
        # if empty
        if ((body.get('name') == "") or (body.get('age') == "")
                or (body.get('gender') == "")):
            abort(422)
        try:
            # create move
            actor = Actors(name=body.get('name', None),
                           age=body.get('age', None),
                           gender=body.get('gender', None))
            actor.insert()
            # return a Response with the JSON representation
            # 'sucsses' , 'create'
            return jsonify({
                'success': True,
                'create': actor.id
            })
        except ex:
            print(ex)
            abort(422)

    '''
         Create an endpoint to DELETE actor using a actor ID.
    '''

    @app.route('/actors/<act_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(jwt, act_id):
        # get actor that matches with act_id
        actor = Actors.query.get(act_id)
        # if there is not such id with this id
        if actor is None:
            abort(422)
        # if exist
        else:
            # delete this movie
            actor.delete()
            # return a Response with the JSON representation
            # 'sucsses' , 'delete'
            return jsonify({
                'success': True,
                'delete': act_id
            })

    '''
         Create an endpoint to update actors using a actor ID.
    '''

    @app.route('/actors/<act_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actors(jwt, act_id):
        # get actor that matches with act_id
        actor = Actors.query.filter(Actors.id == act_id).one_or_none()
        # get the post request data  'name' , 'age' , 'gender'
        body = request.get_json()

        try:
            # update move
            if 'name' in body:
                actor.name = body.get('name', None)
            if 'age' in body:
                actor.age = body.get('age', None)
            if 'gender' in body:
                actor.gender = body.get('gender', None)
            actor.update()
            # return a Response with the JSON representation
            # 'sucsses' , 'update'
            return jsonify({
                'success': True,
                'update': act_id
            })

        except ex:
            print(ex)
            abort(422)
    '''
     Create a GET endpoint to get actors based on move.
    '''
    @app.route('/movies/<act_id>/actors')
    @requires_auth('get:actor_by_movies')
    def get_actor_by_movies(jwt, act_id):

        # get the  movies filtered by actors
        movies = Movies.query.filter(Movies.actors.any(id=act_id)).all()
        if len(movies) == 0:
            abort(404)
        # # make the pagination for every 10 movies)
        # the value of 'PAGINATION_PER_PAGE' variable
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * PAGINATION_PER_PAGE
        end = start + PAGINATION_PER_PAGE
        # # format the questions
        formated_movies = [movie.format() for movie in movies]
        # return a Response with the JSON representation
        # 'sucsses' , 'movies' , 'total_movies'
        return jsonify({
            'success': True,
            'movies': formated_movies[start:end],
            'total_movies': len(movies),
        })
    # set actors to movie

    @app.route('/movies/<movie_id>/actors/<act_id>')
    @requires_auth('add:movies')
    def add_actors_movie(jwt, act_id, movie_id):
        # get actor that matches with act_id
        actor = Actors.query.filter(Actors.id == act_id).one_or_none()
        # if there is not such id with this id
        if actor is None:
            abort(422)
        # get movie that matches with act_id
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        # if there is not such id with this id
        if movie is None:
            abort(422)
        try:
            # create move
            actor.movies.append(movie)
            actor.update()

            # return a Response with the JSON representation
            # 'sucsses' , 'create'
            return jsonify({
                'success': True,
                'create': 'created'
            })
        except ex:
            print(ex)
            abort(422)
    '''

      Create error handlers for all expected errors
      including 404 and 422.
      '''

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def Unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized request"
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(405)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
