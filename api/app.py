from flask import Flask, request
from flask_restful import Resource, Api

from resources.messages import message_api
from resources.users import users_api

from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

import models

app = Flask(__name__)

# ACCESS_TOKEN_JWT
app.config['SECRET_KEY'] = 'randomStringSuperSecret123123'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

jwt = JWTManager(app)

app.register_blueprint(message_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')


# logout hardcode contoh simulasi
blacklist = set()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

@app.route('/api/v1/user/logout')
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return {'msg': 'berhasil logout!'}
    

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True)