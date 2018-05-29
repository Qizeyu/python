import requests as re
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
    print(text)
if __name__ == "__main__":
    main()
