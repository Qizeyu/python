import json
class bitdata:
    def __init__(self,timestamp,price,volume24h,):
        self.timestamp = timestamp;
        self.price     = price;
        self.volume24h = volume24h;
def ToObject(d):
    return bitdata(d['timestamp'],d['price'],d['volume24h'])
jstr='[ { "timestamp" : 1521774900, "price" : 53250.23,"volume24h" : null}, {"timestamp" : 1521775800,"price" : 53234.45,"volume24h" : null}]'
L=json.loads(jstr,object_hook=ToObject)
print(type(L))
for obj in L:
    print('-------->',obj.timestamp)
    print('-------->',obj.price)
    print('-------->',obj.volume24h)
print(L[0].price)
for obj in L:
    if(obj.price<53250.23):
        print("-------->",obj.price)
