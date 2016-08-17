# manage.py


import os
import sys
import getpass
import unittest
import coverage

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from utils import colors

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/server/config.py',
        'project/server/*/__init__.py'
    ]
)
COV.start()

from project.server import app, db
from project.server.models import User


migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    if sys.version_info.major == 3:
        username = input('Your admin username (default: admin) : ') or 'admin'
        email = input('Your admin email address (default: None) : ') or None
        password = getpass.getpass('Your password : ')
        confirm = getpass.getpass('Confirm password : ')

        while password != confirm:
            confirm = getpass.getpass('Confirm password : ')

    else:
        username = raw_input('Your admin username (default: admin) : ') or 'admin'
        email = raw_input('Your admin email address (default: None) : ') or None
        password = getpass.getpass('Your admin password : ')
        confirm = getpass.getpass('Confirm password : ')

        while password != confirm:
            confirm = getpass.getpass('Confirm password : ')


    db.session.add(User(username=username, email=email, password=password, admin=True))
    db.session.commit()
    print('Admin user created...\t\t\t', end="", flush=True)
    print("{green}Ok{end}".format(green=colors.OKGREEN, end=colors.ENDC))



@manager.command
def create_data():
    """Creates sample data."""
    pass


if __name__ == '__main__':
    manager.run()
