import requests
from bs4 import BeautifulSoup

def getHTMLText(url,kv):
   try:
       r=requests.post(url,data=kv)
       r.raise_for_status()
       r.encoding=r.apparent_encoding
       return r.text
   except:
       return ''

def getcontent(html):
    soup=BeautifulSoup(html,'html.parser')
    h3=soup.find('h3').text
    if not u'密码错误' in h3:
        print(html)

def main():
    url='http://www.heibanke.com/lesson/crawler_ex01/'
    for i in range(31):
        print(i)
        kv={'username':'wjl','password':i}
        html=getHTMLText(url,kv)
        getcontent(html)


main()
        
