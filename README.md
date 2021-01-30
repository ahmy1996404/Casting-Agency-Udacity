# Casting Agency Project

## Introduction
Casting Agency is amazing full stack web app project developed for udacity Full-Stack Developer Nanodegree Capstone.
####Casting Agency App Features :-
1) Display movies and actors. 
2) Delete movies and actors.
3) Add movies and actors.
4) edit movies and actors.
5) Display the actor movies.
6) Display the movie actors.
7) Permissions
    - Casting Assistant 
        - Can view actors and movies 
    - Casting Director
        - All permissions a Casting Assistant has and Add or delete an actor from the database Modify actors or movies
    - Executive Producer
        - All permissions a Casting Director has and Add or delete a movie from the database



## Getting Started
### Installing Back-end Dependencies

##### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

##### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

###### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## API Referance
### Getting Start
- Base URL : At present this app run locally and  hosted heroku . The app is hosted at the local , `http://127.0.0.1:5000`,The app is hosted at heroku , `https://casting-agency-uda.herokuapp.com/`
- Authentication : uses Auth0 JWT.
    - AUTH0_DOMAIN
        - ```'ahmedfsnd.us.auth0.com'```
    - ALGORITHMS 
        - ```['RS256']```
    - API_AUDIENCE 
        - ``` 'casting'```
    - Casting_Assistant
      ```
      "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNTY4MzU2OGJmMTgwMDY5ZWRkODkzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMjAxNTgzNywiZXhwIjoxNjEyMTAyMjM3LCJhenAiOiJ1ZTN5N3BZR2JUUXlCRW1FUjdEY1AzUjNDcE1UUUI0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yX2J5X21vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllc19ieV9hY3RvciJdfQ.EZ_LAIWlIiY4IeEF494bd7dhNYOW2quCSx7Jtv6nutKW4oItOLHqLRz1CZWle3Tog3WDpbNvOPBvO5zRVmcTLC9vfuC8edXqEyjr4aEprdQCnBUGmCRiMMfXVc7YKbMUCS5zrnntjR86GX9i_278QMrqOl-nDVCfcCvnMjlpFQcIR75hA6zkzpgMnmVNsS4YNPBTHz4ugYDlJ1CN37jEoDy931P-EJQYuPX-F5gGFI4c8hxwrurpOF1iehGhoqHc3gryEHnw87qvSR2RAumjClVXVympBLUgaot-JdI_FXQH1ONX-tUkBsUN6ISJWprFZIPVhG74jsR-6ia0XYx1kg"
    - Casting_Director 
         ```
        "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNTVlNjY5ZGJkMWEwMDY4ZjA5OWMzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMjAxMzI3MCwiZXhwIjoxNjEyMDk5NjcwLCJhenAiOiJ1ZTN5N3BZR2JUUXlCRW1FUjdEY1AzUjNDcE1UUUI0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yX2J5X21vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllc19ieV9hY3RvciIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWUiXX0.gUyUccANGKhag_N5F3JXfbHNQtbUYN4hdrhUYA513d14Vv6mJIg_1G90_T3Gf2Mqc84-n3HP3sZVKYfTBxywfD3cThfmw706-HAxcCxgwPnTzWaL1pQiCAZ6RpNsBtjsqQjEJsMVZKeEdr5r0lP0E3rXfbbeOEbVkRYgIbwRuWMFaXmu67ICvlJHH57C7o02vjlg9G-l2Wtns7QuJM_c-01f3YTQ3CGJeN0Q9mSuYNefADeOlGjBNC-VOx8zVibmENAbwFJNw80DpSyJtbLOjcsil9LD5M5Vi9w_U_HqQU0f3b2byuB-14N0q4bpv0jVUwyFttyS7DyFupDKlTrhDw"```
    - Executive_Producer
      ```
      "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTAzOTkxNzMzMTc4NjM5OTM0MDciLCJhdWQiOlsiY2FzdGluZyIsImh0dHBzOi8vYWhtZWRmc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTIwMTAwMDEsImV4cCI6MTYxMjA5NjQwMSwiYXpwIjoidWUzeTdwWUdiVFF5QkVtRVI3RGNQM1IzQ3BNVFFCNEsiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3Rvcl9ieV9tb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXNfYnlfYWN0b3IiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllIl19.dxlwEIAWEIenEilqF3mmtlDLe_2wvD--js8mIwrezfW52EQAqqCm_njlfiixEL_IQKsLfuEvIUgkpX1mwhhhJ4KOI9Ng_somhbSARFJxYXPdJs2iQsU6f3EThbup85LAnaHsBeADmjncg1sgD5y3ZCjca33QzDdn30YHyfehqbcsLW3txnfdXNZK-0St6mbwvn4udxbBpui_hgaQFLUV6CYW-Q7WJ7haRFh1j5HlKrgx7R_cl24L2bF6_GCh0IuCPOpqTDP6RiLeVBV6LAKUwAfqWvdnKI2ycIL5u0qzWqjoDx-eEfN2qGMCFyPS1Fc92djjLtj_w7v4cjF6w-F7Jw"```
    - this tokens will be expired
### Error Handling 
Errors are returned as JSON objects in the following format :
```
{
      'success': False,
      'error': 404,
      'message':'resource not found'
}
```
The API will return three error types when requests fail:

- 400: bad request
- 401: Unauthorized request
- 404: resource not found
- 405: method not allowe
- 422: unprocessable
### Endpoint 
#### GET /movies
- General:
    - Returns a list of Movies ( include the actors of this movie , movie id , release_date and title) , total_movies , success value.
- Require
    - header 
        - auth header contain bearer token has permission 'get:movies'
- Sample:
    - `http://127.0.0.1:5000/movies`
    - `https://casting-agency-uda.herokuapp.com/movies`
```
{
    "movies": [
        {
            "actors": [
                {
                    "id": 1,
                    "name": "test name"
                }
            ],
            "id": 1,
            "release_date": "test release_date",
            "title": "test title"
        }
    ],
    "success": true,
    "total_movies": 1
}
```
####POST /movies
- General:
    - Creates a new movie using the title, release_date Returns created movie id  , success value.
- Sample:
    - `http://127.0.0.1:5000/movies`
    - `https://casting-agency-uda.herokuapp.com/movies`
- Require
    - header 
        - Auth header contain bearer token has permission 'add:movies'
        - Content-Type :  application/json
    - data
        - title and release_date
```
{
    "create": 2,
    "success": true
}
```
####DELETE /movies/<movie_id>
- General:
    - Deletes the movie of the given ID if it exists. Returns the id of the deleted movie id, success value.
- Sample:
    - `http://127.0.0.1:5000/movies/<movie_id>`
    - `https://casting-agency-uda.herokuapp.com/movies/<movie_id>`
- Require
    - header 
        - Auth header contain bearer token has permission 'delete:movie'
```
{
  "delete": "2",
  "success": true
}
```
####PATCH /movies/<movie_id>
- General:
    - Edit movie using the movie id  and data . Returns update movie id  , success value.
- Sample:
    - `http://127.0.0.1:5000/movies/<movie_id>`
    - `https://casting-agency-uda.herokuapp.com/movies/<movie_id>`
- Require
    - header 
        - Auth header contain bearer token has permission 'update:movie'
        - Content-Type :  application/json
    - data
        - title or release_date
```
{
  "update": "1",
  "success": true
}
```
####GET /actors/<move_id>/movies
- General:
    - get get actors based on movie with movie id . Returns success value , a list of actor of movie , total number of actors .
- Sample:
    - `http://127.0.0.1:5000/actors/<move_id>/movies`
    - `https://casting-agency-uda.herokuapp.com/actors/<move_id>/movies`
- Require
    - header 
        - Auth header contain bearer token has permission 'get:movies_by_actor'
 
```
{
    "actors": [
        {
            "age": "age",
            "gender": "gender",
            "id": 1,
            "movies": [
                {
                    "id": 1,
                    "title": "movie 1"
                }
            ],
            "name": "test name"
        }
    ],
    "success": true,
    "total_actors": 1
}
```
#### GET /actors
- General:
    - Returns a list of actors ( include the movies of this actor , actor id , age , gender and age) , total_movies , success value.
- Require
    - header 
        - auth header contain bearer token has permission 'get:actors'
- Sample:
    - `http://127.0.0.1:5000/actors`
    - `https://casting-agency-uda.herokuapp.com/actors`
```
{
    "actors": [
        {
            "age": "age",
            "gender": "gender",
            "id": 1,
            "movies": [
                {
                    "id": 1,
                    "title": "movie 1"
                }
            ],
            "name": "test name"
        }
    ],
    "success": true,
    "total_actors": 1
}
```
####POST /actors
- General:
    - Creates a new actor using the name, gender and age  Returns created actor id  , success value.
- Sample:
    - `http://127.0.0.1:5000/actors`
    - `https://casting-agency-uda.herokuapp.com/actors`
- Require
    - header 
        - Auth header contain bearer token has permission 'add:actor'
        - Content-Type :  application/json
    - data
        - name, gender and age
```
{
    "create": 2,
    "success": true
}
```
####DELETE /actors/<act_id>
- General:
    - Deletes the actor of the given ID if it exists. Returns the id of the deleted actor id, success value.
- Sample:
    - `http://127.0.0.1:5000/actor/<act_id>`
    - `https://casting-agency-uda.herokuapp.com/movies/<act_id>`
- Require
    - header 
        - Auth header contain bearer token has permission 'delete:actor'
```
{
  "delete": "2",
  "success": true
}
```
####PATCH /actors/<act_id>
- General:
    - Edit avtor using the avtor id  and data . Returns update actor id  , success value.
- Sample:
    - `http://127.0.0.1:5000/avtor/<act_id>`
    - `https://casting-agency-uda.herokuapp.com/avtor/<act_id>`
- Require
    - header 
        - Auth header contain bearer token has permission 'update:actor'
        - Content-Type :  application/json
    - data
        - name, gender and age
```
{
  "update": "1",
  "success": true
}
```
####GET /movies/<act_id>/actors
- General:
    - get get movies based on actor with actor id . Returns success value , a list of movie of actor , total number of movies .
- Sample:
    - `http://127.0.0.1:5000/movies/<move_id>/actors`
    - `https://casting-agency-uda.herokuapp.com/movies/<move_id>/actors`
- Require
    - header 
        - Auth header contain bearer token has permission 'get:actor_by_movies'
 
```
{
    "movies": [
        {
            "actors": [
                {
                    "id": 1,
                    "name": "actor 1 updated"
                }
            ],
            "id": 1,
            "release_date": "test release_date",
            "title": "movie 1"
        }
    ],
    "success": true,
    "total_movies": 1
}
```
##Authors
Ahmed Hamouda
