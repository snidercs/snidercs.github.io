import shutil
import json
import os

# run this from the util directory

def main(json_file_name: str) -> bool:
    """This is a function that will zip a file and place it in another."""

    try:

        # Defining all of our variables from Json file ZipperSettings.json
        collection = json.load(open(f"{json_file_name}.json"))
        path = collection['Path']
        base_name = collection['FileName']
        what_format = collection['Format']
        root_dir = collection['RootDir']

        # if the path already exists we don't have to make it
        if os.path.exists(path):
            if os.path.exists(f"{path}/{base_name}.{what_format}"):
                # if the zip file already exists delete it
                os.remove(f"{path}/{base_name}.{what_format}")
        # if it doesn't exist, make the path
        else:
            os.mkdir(path)
        # zip our media and move it to the correct directory
        shutil.make_archive(base_name, what_format, root_dir)
        shutil.move(f"{base_name}.{what_format}", path)
        return True
    except FileNotFoundError:
        print("File doesn't exist")
        return False
    except OSError:
        print("Couldn't open specified json")
        return False
    except:
        print("Error")
        return False


if __name__ == "__main__":
    if main("ZipperSettings"):
        print("File zip successful")
    else:
        print("File zip unsuccessful")
