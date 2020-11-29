from flask import jsonify, Blueprint, abort
from flask_restful import Resource, Api, reqparse, fields, marshal, marshal_with

import models

message_fields = {
    'id' : fields.Integer,
    'content': fields.String,
    'published_at': fields.String
}

def get_or_abort(id):
    try:
        msg = models.Message.get_by_id(id)
    except models.Message.DoesNotExist:
        abort(404)
    else:
        return msg

class MessageList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'content',
            required = True,
            help     = 'Konten wajib ada',
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            'published_at',
            required = True,
            help     = 'Tanggal wajib ada',
            location = ['form', 'json']
        )
        super().__init__()

    def get(self):
        # ambil data dari database
        # messages = {}
        # query = models.Message.select()

        # for row in query:
        #     messages[row.id] = {
        #                             'content': row.content,
        #                             'published_at': row.published_at
        #                        }

        # return jsonify({'messages': messages})
        messages = [marshal(message, message_fields) for message in models.Message.select()]

        return {'messages': messages}

    def post(self):
        args = self.reqparse.parse_args()
        message = models.Message.create(**args)
        # return jsonify({'success': True, 'message': message.content})
        return marshal(message, message_fields)


class Message(Resource):
    @marshal_with(message_fields)
    def get(self, id):
        message = models.Message.get_by_id(id)
        return get_or_abort(id)



message_api = Blueprint('resources.messages', __name__)
api         = Api(message_api)

api.add_resource(MessageList, '/messages', endpoint='messages')
api.add_resource(Message, '/message/<int:id>', endpoint='message')