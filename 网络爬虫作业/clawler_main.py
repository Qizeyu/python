import re
import requests
from bs4 import BeautifulSoup
import bs4
import re
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        #print(r.status_code)
        r.encoding = 'utf-8'
        #print(r.text)
        return r.text
    except:
        return ""
def getDataList(datalist,html):
    soup = BeautifulSoup(html,'html.parser')
    i=0
    for tr in soup.find_all('div',attrs={"class":"column"}):
        str1=str(tr.string)
        if str1[0]!="<"and str1[0]!= '\u3000':
            datalist.append(str1)
            #print( str1)
    for te in soup.find_all('div',attrs={"class":"row"}):
        str2=str(te.contents[1])
        if str2[0]!="<":
            datalist.append(str(te.contents[1]))
            #print(te.contents[1])
def openfile():
    urlList=[]
    file = open("urls.txt",'rt')
    for line in file:
        urlList.append(line)
        #print(line)
    file.close()
    return urlList
def dealList(datalist):
    str1=""
    if len(datalist)<=20:
        for i in range(10):
                print(datalist[i],end=" ")
                str1+=datalist[i]
                if i!=8:
                    print(datalist[i+10])
                    str1+=datalist[i+10]+'\n'
                else:
                    print(datalist[i+10][1:-1:])
                    str1+=datalist[i+10][1:-1:]+'\n'
    else:
        for i in range(11):
                print(datalist[i],end=" ")
                str1+=datalist[i]
                if i!=9:
                    print(datalist[i+11])
                    str1+=datalist[i+11]+'\n'
                else:
                    print(datalist[i+11][1:-1:])
                    str1+=datalist[i+11][1:-1:]+'\n'
    str1+='\n'
    #print(str1)
    fo.write(str1)
    print()
def DEAL(urlList):
    for i in range(len(urlList)):
        datalist=[]
        #print(urlList[i])
        urlList[i]=urlList[i].strip()
        html=getHTMLText(urlList[i])
        getDataList(datalist,html)
        datalist =dealList(datalist)
        #print(datalist)
def main():
    global fo
    fo=open('output.txt','w+')
    urlList=openfile()
    DEAL(urlList)
    fo.close()
main()
