import os, sys

KEY = ""
VALUE = ""


#Passed target path
rootpath = sys.argv[1]

from appstore import appstore_handler

store_handler = appstore_handler()
store_handler.set_path(rootpath)

packages = store_handler.get_packages()

for package in packages:
    store_handler.edit_info(package, KEY, VALUE)