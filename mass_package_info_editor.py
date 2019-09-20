import os, sys
from appstore import appstore_handler
store_handler = appstore_handler()

USAGE = "python [Root dir of SD (NOT .get/packages!)] [key to add or change across all packages] [value to set]"

def exit(reason):
    sys.exit("{} Usage - {}".format(reason,USAGE))

#Passed target path
try:
    rootpath = sys.argv[1]
except IndexError:
    exit("SD root path not passed.")
if not rootpath:
    exit("SD root path is empty.")

try:
    key = sys.argv[2]
except IndexError:
    exit("key not passed.")
if not key:
    sys.exit("key is empty.")

try:
    value = sys.argv[3]
except IndexError:
    sys.exit("value not passed.")

store_handler.set_path(rootpath)

packages = store_handler.get_packages()

for package in packages:
    store_handler.edit_info(package, key, value)