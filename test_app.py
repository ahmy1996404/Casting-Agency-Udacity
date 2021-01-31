import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movies, Actors, movies_actors

Casting_Assistant = os.environ['Casting_Assistant']
Casting_Director = os.environ['Casting_Director']
Executive_Producer = os.environ['Executive_Producer']


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://{}/{}"\
            .format('postgres:root@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass
    # test get all movies

    def test_get_movies(self):
        # get response and data
        res = self.client().get('/movies',
                                headers={"Authorization": "Bearer " +
                                                          Casting_Assistant})
        data = json.loads(res.data)

        # check state and sucsses
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    # test error authorization_header_missing

    def test_auth_head_error_get_movies(self):
        # get response and data
        res = self.client().get('/movies')
        data = json.loads(res.data)

        # check state and sucsses
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    # test add movie

    def test_add_movies(self):
        new_movie = {
            'title': 'test title',
            'release_date': 'test release_date'
        }
        res = self.client().post('/movies',
                                 headers={"Authorization": "Bearer " +
                                                           Executive_Producer},
                                 json=new_movie)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test error at permession add movie

    def test_error_auth_movies(self):
        new_movie = {
            'title': 'test title',
            'release_date': 'test release_date',
        }
        res = self.client().post('/movies',
                                 headers={"Authorization": "Bearer " +
                                                           Casting_Assistant},
                                 json=new_movie)
        data = json.loads(res.data)
        # check state and sucsses false
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # test add empty
    def test_empty_add_movies(self):
        new_movie = {
            'title': '',
            'release_date': ''
        }
        res = self.client().post('/movies',
                                 headers={"Authorization": "Bearer " +
                                                           Executive_Producer},
                                 json=new_movie)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # test delete movie

    def test_delete_movie(self):
        # create new movie to delete it
        move = Movies(title='test', release_date='test')
        move.insert()
        # get inserted movie id
        m_id = move.id
        res = self.client().delete('/movies/{}'.format(m_id),
                                   headers={"Authorization": "Bearer " +
                                                             Executive_Producer
                                            })
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test error delete movie

    def test_error_delete_movie_id_not_valid(self):
        # get response and data
        res = self.client().delete('/movies/250',
                                   headers={"Authorization": "Bearer " +
                                                             Executive_Producer
                                            })
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

        # test update movie

    def test_edit_movies(self):
        # create new movie to update it
        move = Movies(title='test', release_date='test')
        move.insert()
        # get inserted movie id
        m_id = move.id
        update_movie = {
            'title': 'update title',
        }
        res = self.client().patch('/movies/{}'.format(m_id),
                                  headers={"Authorization": "Bearer " +
                                                            Executive_Producer
                                           },
                                  json=update_movie)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test error delete movie

    def test_error_update_movie_id_not_valid(self):
        update_movie = {
            'title': 'update title',
        }
        # get response and data
        res = self.client().patch('/movies/250',
                                  headers={"Authorization": "Bearer " +
                                                            Executive_Producer
                                           },
                                  json=update_movie)
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # test get all actors
    def test_get_actors(self):
        # get response and data
        res = self.client().get('/actors',
                                headers={"Authorization": "Bearer " +
                                                          Casting_Assistant
                                         })
        data = json.loads(res.data)

        # check state and sucsses
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test add movie
    def test_add_actors(self):
        new_actors = {
            'name': 'test name',
            'age': 'age',
            'gender': 'gender'
        }
        res = self.client().post('/actors',
                                 headers={"Authorization": "Bearer " +
                                                           Executive_Producer
                                          },
                                 json=new_actors)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test add empty
    def test_empty_add_actors(self):
        new_actors = {
            'name': '',
            'age': '',
            'gender': '',
        }
        res = self.client().post('/actors',
                                 headers={"Authorization": "Bearer " +
                                                           Executive_Producer
                                          },
                                 json=new_actors)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # test delete actor
    def test_delete_actor(self):
        # create new actor to delete it
        actor = Actors(name='test', age='test', gender='test')
        actor.insert()
        # get inserted actor id
        a_id = actor.id
        res = self.client().delete('/actors/{}'.format(a_id),
                                   headers={"Authorization": "Bearer " +
                                                             Executive_Producer
                                            })
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test error delete movie
    def test_error_delete_movie_id_not_valid(self):
        # get response and data
        res = self.client().delete('/actors/250',
                                   headers={"Authorization": "Bearer " +
                                                             Executive_Producer
                                            })
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

        # test update actor

    def test_edit_actor(self):
        # create new actor to update it
        actor = Actors(name='test', age='test', gender='test')
        actor.insert()
        # get inserted actor id
        a_id = actor.id
        update_movie = {
            'name': 'update name',
        }
        res = self.client().patch('/actors/{}'.format(a_id),
                                  headers={"Authorization": "Bearer " +
                                                            Executive_Producer
                                           },
                                  json=update_movie)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test error delete actor
    def test_error_update_actor_id_not_valid(self):
        update_actor = {
            'name': 'update name',
        }
        # get response and data
        res = self.client().patch('/actors/250',
                                  headers={"Authorization": "Bearer " +
                                                            Executive_Producer
                                           },
                                  json=update_actor)
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


if __name__ == '__main__':
    unittest.main()
