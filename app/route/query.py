import sys, os
import falcon
import json
import app.main
  
class routes():
  def __init__(self, api):
    file_name = os.path.splitext(os.path.basename(__file__))[0]
    api.add_route(f'/{file_name}', self)
  #     ici pour charger le modèle une seul X ?
  def on_post(self, req, resp):
    data = json.load(req.bounded_stream)
    # print(data)
    query = data.get('query')
    user_id = req.get_param('user_id')
    save_path = f'var/import/{user_id}'
    result = app.main.query(query, save_path)
    resp.text = json.dumps({'result': result})
    resp.status = falcon.HTTP_201