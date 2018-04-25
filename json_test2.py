import json  
  
d = {'name':'appleyk','sex':'男','age':26}  
  
jstr = json.dumps(d)  
print(jstr)
print(type(jstr))
print('-----上面为json的序列化，下面为json的反序列化-----')  
jsonObject = json.loads(jstr)  
print(jsonObject)
print(type(jsonObject))

