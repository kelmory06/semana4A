# Heroku Python Skeleton

This repository has all the base files ready for deploying a Heroku application, including a simple database model managed with flask-sqlalchemy.

## Usage

### Initial

```bash

$ cd carpeta_proyecto
$ heroku create nombre_proyecto --buildpack heroku/python
$ git init
$ git add .
$ git commit -am "firs-commit"
$ git push heroku master
```

### Database

```bash
$ heroku addons:create heroku-postgresql:hobby-dev
#Attached as HEROKU_POSTGRESQL_COLOR (clave de base de datos)
#heroku pg:promote HEROKU_POSTGRESQL_COLOR (este paso puede que no toque hacerlo)
```
heroku pg:psql
#(copian y pegan todo lo que dice en database.sql)

For a detailed introduction see [http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/](http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/).
