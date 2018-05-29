import requests as re
payload = {'wd':'python'}
r = re.get("https://www.baidu.com/s",params=payload)
print(r.url)

