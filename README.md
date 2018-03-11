# Flask Skeleton

Flask starter project for [Cookiecutter](https://github.com/audreyr/cookiecutter).

[![Build Status](https://travis-ci.org/realpython/cookiecutter-flask-skeleton.svg?branch=master)](https://travis-ci.org/realpython/cookiecutter-flask-skeleton)

## Quick Start

### Basics

Install Cookiecutter globally:

```sh
$ pip install cookiecutter
```

Generate the boilerplate:

```sh
$ cookiecutter https://github.com/realpython/flask-skeleton.git
```

Create and activate a virtual environment, and then install the requirements.

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_NAME="Flask Skeleton"
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
$ export FLASK_DEBUG=1
```

Using pipenv or python-dotenv? Use the *.env* file to set environment variables:

```sh
APP_NAME="Flask Skeleton"
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

###

Run flake8 on the app:

```sh
$ python manage.py flake
```

or 

```
$ flake8 .
```
