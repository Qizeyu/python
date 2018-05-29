import requests as re
from bs4 import BeautifulSoup
def geturl(url):
    w="https://"+url
    try:
        r=re.get(w)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败！")
def main():
    url  ="www.baidu.com"
    #url=input()
    text=geturl(url)
    soup = BeautifulSoup(text)#创建一个BeautifulSoup()对象
    #print(soup.prettify())
    print(soup.p)
    #print(soup.)
    #print(type(soup.prettify()))
if __name__ == "__main__":
    main()
