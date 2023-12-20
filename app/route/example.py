import sys, os
import json
import falcon

class routes():
  def __init__(self, api):
    file_name = os.path.splitext(os.path.basename(__file__))[0]
    api.add_route(f'/{file_name}', self)
  def on_get(self, req, resp):
    resp.content_type = 'application/json'
    result = {"error": "Method not allowed"}
    resp.text = json.dumps(result)