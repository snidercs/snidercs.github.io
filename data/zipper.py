import shutil
import json
import os

# Defining all of our variables from Json file ZipperSettings.json
collection = json.load(open("ZipperSettings.json"))
path = collection['Path']
base_name = collection['FileName']
what_format = collection['Format']
root_dir = collection['RootDir']

# if the path already exists we don't have to make it
if os.path.exists(path):
    if os.path.exists(f"{path}/{base_name}.{what_format}"):
        # if the zip file already exists delete it 
        os.remove(f"{path}/{base_name}.{what_format}")
    # zip our media and move it to the correct directory
    shutil.make_archive(base_name, what_format, root_dir)
    shutil.move(f"{base_name}.{what_format}", path)
# if it doesn't exists, make the path
else:
    os.mkdir(path)
    # zip our media and move it to the correct directory
    shutil.make_archive(base_name, what_format, root_dir)
    shutil.move(f"{base_name}.{what_format}", path)
