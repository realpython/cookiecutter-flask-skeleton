# Setup

Use this guide if you do NOT want to use Docker in your project.

## Getting Started

Create and activate a virtual environment, and then install the requirements.

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_NAME="{{cookiecutter.app_name}}"
$ export APP_SETTINGS="project.server.config.ProductionConfig"
$ export FLASK_DEBUG=0
```
By default the app is set to use the production configuration. If you would like to use the development configuration, you can alter the `APP_SETTINGS` environment variable:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

Using [Pipenv](https://docs.pipenv.org/) or [python-dotenv](https://github.com/theskumar/python-dotenv)? Use the *.env* file to set environment variables:

```
APP_NAME="{{cookiecutter.app_name}}"
APP_SETTINGS="project.server.config.DevelopmentConfig"
FLASK_DEBUG=1
```

### Create DB

```sh
$ python manage.py create-db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create-admin
$ python manage.py create-data
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

Run flake8 on the app:

```sh
$ python manage.py flake
```

or

```sh
$ flake8 project
```
