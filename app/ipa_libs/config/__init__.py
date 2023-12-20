import os
import yaml

configs = {}

def main():
  confs_dir_path = os.path.abspath(os.path.dirname(__file__) + "/../../config")
  for f in os.listdir(confs_dir_path):
    file_name, file_extension = os.path.splitext(f)
    if file_extension == ".yml":
      with open(confs_dir_path + "/" + file_name + file_extension, "r") as ymlfile:
        section = yaml.safe_load(ymlfile)
        configs[file_name] = section

if __name__ != "__main__":
    main()

