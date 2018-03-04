# Flask Skeleton

Flask starter project...

[![Build Status](https://travis-ci.org/realpython/flask-skeleton.svg?branch=master)](https://travis-ci.org/realpython/flask-skeleton)

## Quick Start

### Basics

1. Create and activate a virtualenv
1. Install the requirements


### Configuring

Inspect and update `project/server/config.py`.


### Setting Environment Variables

Eg: for using the development config with debug mode enabled

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
$ export FLASK_DEBUG=1
```

Alternatively using pipenv or python-dotenv you can define your application configuration in the `.env` file.

```sh
APP_SETTINGS="project.server.config.DevelopmentConfig"
FLASK_DEBUG=1
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
$ python manage.py run
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
