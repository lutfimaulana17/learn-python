from flask import Flask, request
from flask_restful import Resource, Api

from resources.messages import message_api
from resources.users import users_api

import models

app = Flask(__name__)

app.register_blueprint(message_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True)