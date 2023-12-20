import json
import falcon
import jwt
from ipa_libs.config import configs
secret_key = configs["jwt"]["secret"] 

class AuthMiddleware:
  def process_request(self, req, resp):
    token = req.get_header('Authorization')
    if req.path == "/auth":
       return
    if not token or not token.startswith('Bearer '):
        resp.status = falcon.HTTP_401
        resp.text = json.dumps({'message': 'Authentication required'})
        resp.complete = True
        return

    token = token.split('Bearer ')[1]
    try:
        # Decode and verify the JWT token
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        username = payload['sub']
        print(username)
    except jwt.ExpiredSignatureError:
        resp.status = falcon.HTTP_401
        resp.text = json.dumps({'message': 'Token has expired'})
        resp.complete = True
        return
    except jwt.InvalidTokenError:
        resp.status = falcon.HTTP_401
        resp.text = json.dumps({'message': 'Invalid token'})
        resp.complete = True
        return