KEY_TO_EDIT = "" #eg compat
NEW_KEY_VALUE = "" #eg 8.1.0

import os, sys, shutil, json
import urllib.request 
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

from appstore import parser, appstore_handler

appstore_repo_url = "https://www.switchbru.com/appstore/repo.json"

#Download a file at a url, returns file path
def download(fileURL, filename):
    try:
        downloadedfile, headers = urllib.request.urlretrieve(fileURL)
        downloadlocation = os.path.join(sys.path[0],filename)
        shutil.move(downloadedfile, downloadlocation)
        print("downloaded {} from url {}".format(filename, fileURL))
        return filename
    except Exception as e: 
        print(e)
        return None

store_json = download(appstore_repo_url, "repo.json")
if not store_json:
    sys.exit("Failed to download appstore json")

repo_parser = parser()
repo_parser.load(store_json)

with open(store_json) as store_json_file:
    store_json_object = json.load(store_json_file)

for package in store_json_object["packages"]:
    package[KEY_TO_EDIT] = NEW_KEY_VALUE

with open("new_repo.json", "w") as new_json_file:
    json.dump(store_json_object, new_json_file)

print(json.dumps(store_json_object, indent = 4))