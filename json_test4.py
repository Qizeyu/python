import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
print(type(data))
json = json.dumps(data)
print(json)
