import urllib
import urllib.request
import json
class bitdata:
    def __init__(self,timestamp,price,volume24h,):
        self.timestamp = timestamp;
        self.price     = price;
        self.volume24h = volume24h;
def ToObject(d):
    return bitdata(d['timestamp'],d['price'],d['volume24h'])
def getHtmlData(url):
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'}  
    request = urllib.request.Request(url, headers=headers)  
    response = urllib.request.urlopen(request)  
    data = response.read()  
    # 设置解码方式  
    data = data.decode('utf-8')  
    return data
url = "https://api.blockchain.info/price/index-series?base=btc&quote=CNY&start=1521774455&scale=900"
data=getHtmlData(url)
#print(data)
L=json.loads(data,object_hook=ToObject)
for obj in L:
    print('-------->',obj.timestamp)
    print('-------->',obj.price)
    print('-------->',obj.volume24h)
print(type(L))
