################################################################################
"""                        Author(s): Riley Conrardy                         """
################################################################################

import os
import boto3
import flask
import flask_sqlalchemy
import flask_socketio
import flask_login
import flask_mail


################################################################################
"""                            Application Setup                             """
################################################################################

# boto3
s3 = boto3.client('s3', region_name='us-east-2')

# flask
app = flask.Flask(__name__)
app.config.from_object('config')

# flask_login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# flask_mail
mail = flask_mail.Mail(app)

# flask_socketio
socketio = flask_socketio.SocketIO(app)

# flask_sqlalchemy
db = flask_sqlalchemy.SQLAlchemy(app)

# views and api
import quickstart.views
import quickstart.api
