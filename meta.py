import json
import os

json_file = open('data/meta.txt')

meta = json.load(json_file)

Group = meta['Group']
FILE_NAME_DISK = meta['FILE_NAME_DISK']
API_KEY = meta['API_KEY']
SECRET = meta['SECRET']




