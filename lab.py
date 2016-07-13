from flask import Flask
from flask_admin import Admin
from flask_admin.contrib import sqla
from model.model import *


def build_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456790'

    # Create in-memory database
    app.config['DATABASE_FILE'] = 'basic_db.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
    app.config['SQLALCHEMY_ECHO'] = True

    db.app = app
    db.init_app(app)

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
