import shutil
import json
import os

collection = json.load(open("ZipperSettings.json"))
path = collection['Path']
base_name = collection['FileName']
what_format = collection['Format']
root_dir = collection['RootDir']

if os.path.exists(path):
    if os.path.exists(f"{path}/{base_name}.{what_format}"):
        os.remove(f"{path}/{base_name}.{what_format}")
    shutil.make_archive(base_name, what_format, root_dir)
    shutil.move(f"{base_name}.{what_format}", path)
else:
    os.mkdir(path)
    shutil.make_archive(base_name, what_format, root_dir)
    shutil.move(f"{base_name}.{what_format}", path)
