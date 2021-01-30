import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db , Movies , Actors , movies_actors

Casting_Assistant="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNTY4MzU2OGJmMTgwMDY5ZWRkODkzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMjAxNTgzNywiZXhwIjoxNjEyMTAyMjM3LCJhenAiOiJ1ZTN5N3BZR2JUUXlCRW1FUjdEY1AzUjNDcE1UUUI0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yX2J5X21vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllc19ieV9hY3RvciJdfQ.EZ_LAIWlIiY4IeEF494bd7dhNYOW2quCSx7Jtv6nutKW4oItOLHqLRz1CZWle3Tog3WDpbNvOPBvO5zRVmcTLC9vfuC8edXqEyjr4aEprdQCnBUGmCRiMMfXVc7YKbMUCS5zrnntjR86GX9i_278QMrqOl-nDVCfcCvnMjlpFQcIR75hA6zkzpgMnmVNsS4YNPBTHz4ugYDlJ1CN37jEoDy931P-EJQYuPX-F5gGFI4c8hxwrurpOF1iehGhoqHc3gryEHnw87qvSR2RAumjClVXVympBLUgaot-JdI_FXQH1ONX-tUkBsUN6ISJWprFZIPVhG74jsR-6ia0XYx1kg"
Executive_Producer= "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTAzOTkxNzMzMTc4NjM5OTM0MDciLCJhdWQiOlsiY2FzdGluZyIsImh0dHBzOi8vYWhtZWRmc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTIwMTAwMDEsImV4cCI6MTYxMjA5NjQwMSwiYXpwIjoidWUzeTdwWUdiVFF5QkVtRVI3RGNQM1IzQ3BNVFFCNEsiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3Rvcl9ieV9tb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXNfYnlfYWN0b3IiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllIl19.dxlwEIAWEIenEilqF3mmtlDLe_2wvD--js8mIwrezfW52EQAqqCm_njlfiixEL_IQKsLfuEvIUgkpX1mwhhhJ4KOI9Ng_somhbSARFJxYXPdJs2iQsU6f3EThbup85LAnaHsBeADmjncg1sgD5y3ZCjca33QzDdn30YHyfehqbcsLW3txnfdXNZK-0St6mbwvn4udxbBpui_hgaQFLUV6CYW-Q7WJ7haRFh1j5HlKrgx7R_cl24L2bF6_GCh0IuCPOpqTDP6RiLeVBV6LAKUwAfqWvdnKI2ycIL5u0qzWqjoDx-eEfN2qGMCFyPS1Fc92djjLtj_w7v4cjF6w-F7Jw"
Casting_Director ="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNTVlNjY5ZGJkMWEwMDY4ZjA5OWMzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMjAxMzI3MCwiZXhwIjoxNjEyMDk5NjcwLCJhenAiOiJ1ZTN5N3BZR2JUUXlCRW1FUjdEY1AzUjNDcE1UUUI0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yX2J5X21vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllc19ieV9hY3RvciIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWUiXX0.gUyUccANGKhag_N5F3JXfbHNQtbUYN4hdrhUYA513d14Vv6mJIg_1G90_T3Gf2Mqc84-n3HP3sZVKYfTBxywfD3cThfmw706-HAxcCxgwPnTzWaL1pQiCAZ6RpNsBtjsqQjEJsMVZKeEdr5r0lP0E3rXfbbeOEbVkRYgIbwRuWMFaXmu67ICvlJHH57C7o02vjlg9G-l2Wtns7QuJM_c-01f3YTQ3CGJeN0Q9mSuYNefADeOlGjBNC-VOx8zVibmENAbwFJNw80DpSyJtbLOjcsil9LD5M5Vi9w_U_HqQU0f3b2byuB-14N0q4bpv0jVUwyFttyS7DyFupDKlTrhDw"

class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://{}/{}".format('postgres:root@localhost:5432', self.database_name)
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
        res = self.client().get('/movies',headers={"Authorization": "Bearer " + Casting_Assistant})
        data = json.loads(res.data)

        # check state and sucsses
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
    # test error authorization_header_missing
    def test_auth_head_error_get_movies(self):
        # get response and data
        res = self.client().get('/movies')
        data = json.loads(res.data)

        # check state and sucsses
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'],False)
    # test add movie
    def test_add_movies(self):
        new_movie={
            'title': 'test title',
            'release_date': 'test release_date',
        }
        res = self.client().post('/movies',headers={"Authorization": "Bearer " + Executive_Producer},json=new_movie)
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
        res = self.client().post('/movies', headers={"Authorization": "Bearer " + Casting_Assistant}, json=new_movie)
        data = json.loads(res.data)
        # check state and sucsses false
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

# test add empty
    def test_empty_add_movies(self):
        new_movie={
            'title': '',
            'release_date': '',
        }
        res = self.client().post('/movies',headers={"Authorization": "Bearer " + Executive_Producer},json=new_movie)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
  # test delete movie
    def test_delete_movie(self):
        # create new movie to delete it
        move = Movies(title='test' , release_date= 'test')
        move.insert()
        # get inserted movie id
        m_id = move.id
        res = self.client().delete('/movies/{}'.format(m_id),headers={"Authorization": "Bearer " + Executive_Producer})
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    # test error delete movie
    def test_error_delete_movie_id_not_valid(self):
        # get response and data
        res = self.client().delete('/movies/250',headers={"Authorization": "Bearer " + Executive_Producer})
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'],False)

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
        res = self.client().patch('/movies/{}'.format(m_id), headers={"Authorization": "Bearer " + Executive_Producer}, json=update_movie)
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
        res = self.client().patch('/movies/250',headers={"Authorization": "Bearer " + Executive_Producer}, json=update_movie)
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'],False)

    # test get all actors
    def test_get_actors(self):
        # get response and data
        res = self.client().get('/actors', headers={"Authorization": "Bearer " + Casting_Assistant})
        data = json.loads(res.data)

        # check state and sucsses
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test add movie
    def test_add_actors(self):
        new_actors = {
            'name': 'test name',
            'age': 'age',
            'gender': 'gender',
        }
        res = self.client().post('/actors', headers={"Authorization": "Bearer " + Executive_Producer}, json=new_actors)
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
        res = self.client().post('/actors', headers={"Authorization": "Bearer " + Executive_Producer}, json=new_actors)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # test delete actor
    def test_delete_actor(self):
        # create new actor to delete it
        actor = Actors(name='test', age='test' , gender='test')
        actor.insert()
        # get inserted actor id
        a_id = actor.id
        res = self.client().delete('/actors/{}'.format(a_id), headers={"Authorization": "Bearer " + Executive_Producer})
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # test error delete movie
    def test_error_delete_movie_id_not_valid(self):
        # get response and data
        res = self.client().delete('/actors/250', headers={"Authorization": "Bearer " + Executive_Producer})
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

        # test update actor

    def test_edit_actor(self):
        # create new actor to update it
        actor = Actors(name='test', age='test' , gender='test')
        actor.insert()
        # get inserted actor id
        a_id = actor.id
        update_movie = {
            'name': 'update name',
        }
        res = self.client().patch('/actors/{}'.format(a_id), headers={"Authorization": "Bearer " + Executive_Producer},
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
        res = self.client().patch('/actors/250', headers={"Authorization": "Bearer " + Executive_Producer},
                                  json=update_actor)
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


if __name__ == '__main__':
    unittest.main()

