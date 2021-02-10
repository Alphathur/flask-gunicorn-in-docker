# flask-gunicorn-in-docker
A Restful application using flask and gunicorn running in docker, and fetching data from mysql

## Run in local
```bash
python apps/main.py
```

## Run in docker
### Start Mysql and import data
```bash
docker network create mysql-network
docker run -d  -p 3306:3306 -e MYSQL_ROOT_PASSWORD=mysql520  -v /opt/data/mysql:/var/lib/mysql --name mariadb --net=mysql-network  --network-alias mysql  mariadb:10.3
docker cp student.sql mariadb:.
docker exec -it mariadb /bin/bash
mysql -hlocalhost -uroot -pmysql520
```
```bash
create database demo;
use demo;
source user.sql;
```
### Run Flask application and Gunicorn in docker
```bash
docker build -t flask-gunicorn-in-docker:1.0 .
docker run -d -p8000:8000 --name flask-gunicorn-in-docker --net=mysql-network data-api:1.0
```

## Test your api
```bash
curl 'http://localhost:8000/'
Hello World
```
```bash
curl 'http://localhost:8000/students'
[
  {
    "age": 22, 
    "birth": "Wed, 24 Jun 1998 00:00:00 GMT", 
    "gender": "1", 
    "id": 1, 
    "name": "Andrew", 
    "parent": "Sony"
  }, 
  {
    "age": 21, 
    "birth": "Sun, 24 Jan 1999 00:00:00 GMT", 
    "gender": "0", 
    "id": 2, 
    "name": "Tom", 
    "parent": "Jackie"
  }, 
  {
    "age": 20, 
    "birth": "Wed, 24 Nov 1920 00:00:00 GMT", 
    "gender": "1", 
    "id": 3, 
    "name": "Johnson", 
    "parent": "Mickey"
  }
]
```
