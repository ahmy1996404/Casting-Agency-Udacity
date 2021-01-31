# Casting Agency Project

## Introduction
Casting Agency is amazing full stack web app project developed for udacity Full-Stack Developer Nanodegree Capstone , The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
## Motivation 
#### Why did I make this project?
I developed this project to make use of the knowledge i acquired in this nanodegree and hence gain confidence in these skills.
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
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

###### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

###Local Database Setup
Once you create the database, open your terminal, navigate to the root folder, and run:
```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
After running, don't forget modify 'SQLALCHEMY_DATABASE_URI' variable.

###Local Testing
To test your local installation, run the following command from the root folder:
```
python -m test_app.py
```
If all tests pass, your local installation is set up correctly.

###Running the server
From within the root directory, first ensure you're working with your created
venv. To run the server, execute the following:
```
export FLASK_APP=manage
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run
```
Setting the ```FLASK_ENV``` variable to development will detect file changes and
restart the server automatically.
Setting the ```FLASK_APP``` variable to ```manage``` directs Flask to use
the ``` manage``` directory and the __init__.py file to find and load the
application.
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
      "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNTY4MzU2OGJmMTgwMDY5ZWRkODkzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMjA3ODY4NiwiZXhwIjoxNjEyMTY1MDg2LCJhenAiOiJ1ZTN5N3BZR2JUUXlCRW1FUjdEY1AzUjNDcE1UUUI0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yX2J5X21vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllc19ieV9hY3RvciJdfQ.Vcs8NjdqD599x4rPWzzqvQWaPE4blQtFEtNNwgRNbKiNQPfyaAPCzL7Ii5f1PGQOFF17kxt32AbszMzrHZr1U_erxWpRWbU5hitPheLbgLJCIY8KY2erA580rZU93m3wGaavImlbdVi8q7tWHoLD2gepVHjC1G8ytca1qxKUHTFGlquMtx15BFlUC7JD0SzEIP4-VDW6xoNzcqPVW31sizkFr7d_pRZHvFgW9unctis3aDZzgQMc78Zr3_YIB56O1uYOtakfoHc-CjjYS5Qw_qHoOrDzeqV9QBwqQj_drPdLONPiXHtgAXfbwCL4YwjtGBtuH-69nP8U6WLw_a25OQ"
    - Casting_Director 
         ```
        "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNTVlNjY5ZGJkMWEwMDY4ZjA5OWMzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMjA3ODM3MiwiZXhwIjoxNjEyMTY0NzcyLCJhenAiOiJ1ZTN5N3BZR2JUUXlCRW1FUjdEY1AzUjNDcE1UUUI0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yX2J5X21vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllc19ieV9hY3RvciIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWUiXX0.cVkqlhcjqxIjuXv1R3wwq8T-8QIhj0KWFIEWyMddkNRxWZ4EpTee2Uf4bbZl5eMl0Xy2Evh-GjL1GBb-fDnXVUUZuEDAypUl4syKW58spFaIcBH7-UjPc0C8zgLXk1j5npT4ZrRWrodd_5XQIcJc6yotbWbVTeEzE03vle8NsfJ76xltqWsvTnICh0zFy5XOdY_7ROpIWNIeH6X8k6kr4JhLY_Y7sViW1fisrFLsDaXorJys-cuxp_G2BIfD31GaNAjB9lfPuXTHTRt59RuChTXoQecoVWIFCRBM66D-tGCOxFtc5VnmzTwwkGDgxT6osIsEkw1FDpdSIPWsRIeylg"```
    - Executive_Producer
      ```
      "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZ2TG5XbmxjaVJqZFVkVjY5bmpvQiJ9.eyJpc3MiOiJodHRwczovL2FobWVkZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTAzOTkxNzMzMTc4NjM5OTM0MDciLCJhdWQiOlsiY2FzdGluZyIsImh0dHBzOi8vYWhtZWRmc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTIwNzgyMzYsImV4cCI6MTYxMjE2NDYzNiwiYXpwIjoidWUzeTdwWUdiVFF5QkVtRVI3RGNQM1IzQ3BNVFFCNEsiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3Rvcl9ieV9tb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXNfYnlfYWN0b3IiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllIl19.hmc_AlTsnO8K-LRnnKK3NxjBKKLZJ4nvtbQoP31Z7TMxyEVp_eDEj8q2Xrfh10uT6nIyh1ct5xessPzwdC3kJSRM4163T_rnOxkbNzZfq7oJ8qLadRDx_N70NU4DEPNz2n-vT4jhVOzNX3o5hJLnTFUHZDAdUijhaSuYb6munovg4aa5Yo_uU4IdhkcfDfKvg9ykudPOjhcG_rMmgIQo8wml-yqsvtZ2X3xLXpksWnaPAhvYToHdg3_Z_vDThzhfVD-yUXoitZ0KL_cl-LTcuS87g_vPFkgfmru-l-fA-m6-vcv_ZwqvGBsG8Oc-fGn26F3adIV1mJ58GllMkhMq0g"```
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
