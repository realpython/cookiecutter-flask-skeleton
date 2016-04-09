# Flask Skeleton

Flask starter project...

[![Build Status](https://travis-ci.org/realpython/flask-skeleton.svg?branch=master)](https://travis-ci.org/realpython/flask-skeleton)

## Quick Start

### Basics

1. Activate a virtualenv
1. Install the requirements

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)

Or

### Run the Application in a specific port enabling connections via ip address

```sh
$ python manage.py runserver -h 0.0.0.0 -p 80
```

So access the application at the address [http://127.0.0.1:8080/](http://127.0.0.1:8080/)


### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
