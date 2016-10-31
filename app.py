# -*- coding: utf-8 -*-
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib import sqla
from model.model import *
from reverseproxy import ReverseProxied


def build_app():
    app = Flask(__name__)

    app.config.from_object('config.LocalConfig')

    db.app = app

    db.init_app(app)

    app.wsgi_app = ReverseProxied(app.wsgi_app)

    return app

app = build_app()


class UserView(sqla.ModelView):
    can_edit = True


admin = Admin(app, name='microblog', template_mode='bootstrap3')

admin.add_view(UserView(User, db.session))

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run()


