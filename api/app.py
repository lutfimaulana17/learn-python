from flask import Flask, request
from flask_restful import Resource, Api
from resources.messages import message_api

import models

app = Flask(__name__)
# api = Api(app)
# api.add_resource(messages.MessageList, '/messages')

app.register_blueprint(message_api, url_prefix='/api/v1')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True)