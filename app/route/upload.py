import sys, os
import falcon
import json
from werkzeug.utils import secure_filename
  
class routes():
  def __init__(self, api):
    file_name = os.path.splitext(os.path.basename(__file__))[0]
    api.add_route(f'/{file_name}', self)
  def on_post(self, req, resp):
    #https://github.com/yohanboniface/falcon-multipart
    user_id = req.get_param('user_id')
    save_path = f'var/import/{user_id}'
    if not os.path.exists(save_path):
      os.makedirs(save_path)
    uploaded_files = req.get_param_as_list('file')

    if uploaded_files:
      # Loop through and save each uploaded file
      for file in uploaded_files:
        filename = secure_filename(file.filename)
        if not filename:
          resp.status = falcon.HTTP_BAD_REQUEST
          resp.body = 'Filename missing'
        with open(f'{save_path}/{filename}', "wb") as binary_file:
          binary_file.write(file.value)
        
    resp.status = falcon.HTTP_201