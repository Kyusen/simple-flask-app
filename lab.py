import dateutil.parser

from flask import Flask, render_template
from flask_adminlte import AdminLTE
from model.model import *

class User(object):
    """
    Example User object.  Based loosely off of Flask-Login's User model.
    """
    full_name = "John Doe"
    avatar = "/static/img/user2-160x160.jpg"
    created_at = dateutil.parser.parse("November 12, 2012")


def create_app(configfile=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456790'

    # Create in-memory database
    app.config['DATABASE_FILE'] = 'basic_db.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
    app.config['SQLALCHEMY_ECHO'] = True
    AdminLTE(app)
    db.app = app
    db.init_app(app)
    # This is a placeholder user object.  In the real-world, this would
    # probably get populated via ... something.
    current_user = User()

    @app.route('/')
    def index():
        return render_template('index.html', current_user=current_user)

    @app.route('/login')
    def login():
        return render_template('login.html', current_user=current_user)

    @app.route('/lockscreen')
    def lockscreen():
        return render_template('lockscreen.html', current_user=current_user)

    return app

if __name__ == '__main__':
    #db.create_all()
    #db.session.commit()
    create_app().run(debug=True)


