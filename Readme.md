# Youtube Search API Support:

  A Simple search and response System from Youtube, 
  it's suppose to search the videos according to the keyword 
  provided by the user
  and system should store the attributes of the video in the Database
  and it should return the response in paginated way in descreasing order of Datetime


## Run Application without Docker

```
$ Virtualenv env -p python3
$ source ~/env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver

$ Get - http://localhost:8000/search
```


## Run Application with Docker

```
$ docker build --tag fampayyoutubesearch .
$ docker run --publish 8000:8000 fampayyoutubesearch

$ Get - http://localhost:8000/search
```

 
## Operations Allowed

 ## Simple Search
 http://localhost:8000/search/
 ## Search with title
 http://localhost:8000/search/?title=Road To 175K!!!  Natasha Gaming PUBG Live
 ## search with description
 http://localhost:8000/search/?description=Telugu/Hindi Girl Gamer is Live Streaming PUBG Mobile. Hey! This is Natasha. Natasha Gaming is Live. Please join. I stream pubg mobile and some of the PC ...
 ## search with title and description
 http://localhost:8000/search/?title=Road To 175K!!!  Natasha Gaming PUBG Live&description=Telugu/Hindi Girl Gamer is Live Streaming PUBG Mobile. Hey! This is Natasha. Natasha Gaming is Live. Please join. I stream pubg mobile and some of the PC ...
