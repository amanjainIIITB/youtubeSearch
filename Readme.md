# Role Based Access Control:

  A Simple search and response System from Youtube, 
  it suppose to search the videos according to the keyword 
  provided by the user in the POST call 
  and system should store the attributes in the Database
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
$ docker build -t youtubesearch .
$ docker run -ti youtubesearch

$ Get - http://localhost:8000/search
```

 
## Operations Allowed

 - Simple Search# youtubeSearch
