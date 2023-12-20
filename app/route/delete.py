import sys, os
import glob
import falcon
import json
from werkzeug.utils import secure_filename
  
class routes():
  def __init__(self, api):
    file_name = os.path.splitext(os.path.basename(__file__))[0]
    api.add_route(f'/{file_name}', self)
  def on_get(self, req, resp):
    user_id = req.get_param('user_id')
    save_path = f'var/import/{user_id}'
    files = glob.glob(f'{save_path}/*')
    for f in files:
     os.remove(f)
    resp.status = falcon.HTTP_201