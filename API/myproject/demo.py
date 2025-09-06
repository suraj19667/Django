import json

'''Inbuild method json
dump()
dumps()
load()
loads()

python-data -> json.dumps()->json data
json-data -> json.loads() -> python-data

'''
j_data='{"1":true,"2":false,"3":null}'

p_data=json.loads(j_data)
print(p_data)
print(type(p_data))
