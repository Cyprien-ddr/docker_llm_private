import sys, os
import importlib
local_path = os.path.abspath(os.path.dirname(__file__) + "/../../")
sys.path.insert(0, local_path)

def all(api):
  for f in os.listdir(f'{local_path}/route'):
    file_name, file_extension = os.path.splitext(f)
    if not file_name.endswith('__init__') and not file_name.endswith('__pycache__'):
      route = importlib.import_module(f'route.{file_name}')
      route.routes(api)
      #api.add_route(f'/{file_name}', route.routes())
  




