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
    url  ="www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book"
    #url=input()
    text=geturl(url)
    #print(text)
    soup=BeautifulSoup(text,"html.parser")
    book_div = soup.find(attrs={"id":"book"})
    book_a = book_div.findAll(attrs={"class":'title'})
    book_b = book_div.findAll(attrs={"class":"desc"})
    for book in book_a:
        print(book.string)
    for book in book_b:
        print(book.string)

if __name__ == "__main__":
    main()
