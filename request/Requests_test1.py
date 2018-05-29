import requests as re
r = re.get("https://www.baidu.com")
#HTTP中最常被用到的方法是GET和POST
#GET-指定的资源处请求数据               -查
#POST-向指定的资源提交要被处理的数据    -增
#print(type(r))

#print(r.status_code)

#print(type(r.text))

#print(r.text)
#print(r.encoding)
#print(r.apparent_encoding)
#print(r.text)
r.encoding = r.apparent_encoding
print(r.text)
#print(r.cookies)
#print(r.content)
#print(r.url)
#print(r.content.decode("utf-8"))'''
