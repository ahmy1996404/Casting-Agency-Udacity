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
    - Returns a list of categories objects, success value.
- Sample:
    - `curl http://127.0.0.1:5000/movies`
    - `curl http://127.0.0.1:5000/movies`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```
#### GET /questions
- General:
    - Returns success value , a list of questions objects, total number of questions and a list of categories objects .
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: 
    - `curl http://127.0.0.1:5000/questions`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 22
}
```
####DELETE /questions/{question_id}
- General:
    - Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value.
```
{
  "delete": "22",
  "success": true
}
```
####POST /questions
- General:
    - Creates a new question using the submitted question, answer , category and difficulty. Returns created quistion id  , success value.
- Sample:
    - ` curl -i -X POST -H "Content-Type: application/json" -d "{\"question\":\"test q\",\"answer\":\"test a\",\"category\":1,\"difficulty\":5}" http://127.0.0.1:5000/questions`
```
{
  "create": 21 ,
  "success": true
}
```
####POST /questions/search
- General:
    - search for  questions matches with searchTerm  using searchTerm and current category if null that mean all categories . Returns success value , a list of questions objects, total number of questions .
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample:
    - ` curl -i -X POST -H "Content-Type: application/json" -d "{\"searchTerm\":\"title\" , \"currentCategory\": null}" http://127.0.0.1:5000/questions/search`
```
                                                                                                                                             
{                                                                                                                                            
  "currentCategory": null,                                                                                                                   
  "questions": [                                                                                                                             
    {                                                                                                                                        
      "answer": "Maya Angelou",                                                                                                              
      "category": 4,                                                                                                                         
      "difficulty": 2,                                                                                                                       
      "id": 5,                                                                                                                               
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"                                                       
    },                                                                                                                                       
    {                                                                                                                                        
      "answer": "Edward Scissorhands",                                                                                                       
      "category": 5,                                                                                                                         
      "difficulty": 3,                                                                                                                       
      "id": 6,                                                                                                                               
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"            
    }                                                                                                                                        
  ],                                                                                                                                         
  "success": true,                                                                                                                           
  "total_questions": 2                                                                                                                       
}                                                                                                                                            
                                                                                                                                             
```
#### GET /categories/<cat_id>/questions
- General:
    - Get questions of category use cat_id,  Returns success value , a list of questions based on category  , total number of questions , current_category .
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: 
    - `curl http://127.0.0.1:5000/categories/1/questions`
```
{                                                                          
  "current_category": "1",                                           
  "questions": [                                                           
    {                                                                      
      "answer": "The Liver",                                               
      "category": 1,                                                       
      "difficulty": 4,                                                     
      "id": 20,                                                            
      "question": "What is the heaviest organ in the human body?"          
    },                                                                     
    {                                                                      
      "answer": "Alexander Fleming",                                       
      "category": 1,                                                       
      "difficulty": 3,                                                     
      "id": 21,                                                            
      "question": "Who discovered penicillin?"                             
    },                                                                     
    {                                                                      
      "answer": "test a",                                                  
      "category": 1,                                                       
      "difficulty": 5,                                                     
      "id": 24,                                                            
      "question": "test q"                                                 
    },                                                                     
    {                                                                      
      "answer": "test2 a",                                                 
      "category": 1,                                                       
      "difficulty": 5,                                                     
      "id": 25,                                                            
      "question": "test2 q"                                                
    },                                                                     
    {                                                                      
      "answer": "test2 a",                                                 
      "category": 1,                                                       
      "difficulty": 5,                                                     
      "id": 33,                                                            
      "question": "test2 q"                                                
    },                                                                     
    {                                                                      
      "answer": "test2 a",                                                 
      "category": 1,                                                       
      "difficulty": 5,                                                     
      "id": 35,                                                            
      "question": "test2 q"                                                
    }                                                                      
  ],                                                                       
  "success": true,                                                         
  "total_questions": 6                                                     
}                                                                          
```
####POST /quizzes
- General:
    -  get questions to play the quiz using category and previous question . Returns success value ,a random questions within the given category, 
  if provided, and that is not one of the previous questions .
- Sample
    - `curl -i -X POST -H "Content-Type: application/json" -d "{\"quiz_category\":{\"type\": \"Science\", \"id\": \"1\"},\"previous_questions\":[1,2]}" http://127.0.0.1:5000/quizzes`
 ```
{
  "question": {
    "answer": "The Liver",
    "category": 1,
    "difficulty": 4,
    "id": 20,
    "question": "What is the heaviest organ in the human body?"
  },
  "success": true
}
``` 
##Authors
Ahmed Hamouda
