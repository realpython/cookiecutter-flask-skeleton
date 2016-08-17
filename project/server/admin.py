# project/server/admin/views.py
import datetime

from flask import Blueprint, request, url_for, flash, render_template, redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, helpers, expose, AdminIndexView
from flask_login import login_user, logout_user, current_user

from project.server import db, app, bcrypt
from project.server.models import User
from project.server.user.forms import LoginForm

###################
### blueprints ####
###################

admin_blueprint = Blueprint('administration', __name__)

###################
##  config auth ###
###################


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_authenticated: #if user is authenticated
            user = current_user.admin
            if user == False: #if user is not admin, user is logout automaticaly
                logout_user()
                return redirect(url_for('admin.login_view'))
        if not current_user.is_authenticated:
            return redirect(url_for('admin.login_view'))
        return super(MyAdminIndexView, self).index()


    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            if user.admin == True: #if user is admin, user is_authenticated and can use admin interface
                login_user(user)
            else:
                flash('You are not admin to enter here!', 'danger')
                return redirect(url_for('admin.index'))

        if current_user.is_authenticated:
            flash('You are logged in. Welcome!', 'success')
            return redirect(url_for('admin.index'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()


    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('main.home'))


###################
##  models class ##
###################

class UserView(MyModelView):
    can_create = False
    edit_modal = True
    page_size = 20
    column_searchable_list = ['username',]
    column_exclude_list = ['password',]

###################
#### init admin ###
###################

admin = Admin(app, name='flask-skeleton',
                index_view=MyAdminIndexView(),
                base_template='admin/my_master.html',
                template_mode='bootstrap3')

admin.add_view(UserView(User, db.session))
