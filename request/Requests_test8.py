from bs4 import BeautifulSoup
import requests as re
def geturl(url):
    w="https://"+url
    try:
        r=re.get(w)
        #r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败！")
def main():
    url = 'store.steampowered.com/tags/zh-cn/%E4%BC%91%E9%97%B2/'
    text=geturl(url)
    #print(text)
    soup=BeautifulSoup(text,"html.parser")
    b=soup.find_all(attrs={"class":"tab_item_name"})
    for i in b:                             
        print(i.string)
    
if __name__ == "__main__":
    main()
