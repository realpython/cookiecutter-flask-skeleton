# Flask Skeleton

Flask starter project...

[![Build Status](https://travis-ci.org/realpython/flask-skeleton.svg?branch=master)](https://travis-ci.org/realpython/flask-skeleton)

## Quick Start

### Set Environment Variables

Update the configuration setting files in "/project/config" and then run:

```sh
$ export APP_SETTINGS="project.config.development_config"
```

or

```sh
$ export APP_SETTINGS="project.config.production_config"
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
