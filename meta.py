import json

json_file = open('data/meta.txt')

meta = json.load(json_file)

Group = meta['Group']
FILE_NAME_DISK = meta['FILE_NAME_DISK']




