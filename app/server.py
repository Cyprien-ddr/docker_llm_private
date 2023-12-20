#!/usr/bin/env python3
import falcon
from falcon_multipart.middleware import MultipartMiddleware
from app.auth import AuthMiddleware
from ipa_libs.routing import publish
    
api = falcon.App(middleware=[MultipartMiddleware(), AuthMiddleware()])
api.req_options.auto_parse_form_urlencoded=True
api.req_options.auto_parse_qs_csv = True
publish.all(api)

def debug(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    # Get the request body by reading from the input stream
    request_body = environ['wsgi.input'].read()

    # Print the request body
    print("Request Body:")
    print(request_body.decode('utf-8'))  # Assuming UTF-8 encoding

    # Return a response
    return [b'Request body printed']

if __name__ == '__main__':
    # Juste pour tester en local, en prod c'est gunicron le server http
    from wsgiref.simple_server import make_server
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')
        # Serve until process is killed
        httpd.serve_forever()
