import sys, os
import json
import falcon
import jwt
from datetime import datetime, timedelta, timezone
from ipa_libs.config import configs
# Secret key for JWT encoding and decoding
secret_key = configs["jwt"]["secret"] 
api_users = configs["api_users"]["users"] 



class routes():
    def __init__(self, api):
        file_name = os.path.splitext(os.path.basename(__file__))[0]
        api.add_route(f'/{file_name}', self)
    def on_post(self, req, resp):
        data = json.load(req.bounded_stream)
        username = data.get('user')
        password = data.get('password')
        if username in api_users and api_users[username] == password:
            # Generate a JWT token
            expire = datetime.now(tz=timezone.utc) + timedelta(hours=1)
            token = jwt.encode({'sub': username, 'exp': expire}, secret_key, algorithm='HS256')
            resp.status = falcon.HTTP_200
            resp.text = json.dumps({'access_token': token})
        else:
            resp.status = falcon.HTTP_401
            resp.text = json.dumps({'message': 'Invalid credentials'})