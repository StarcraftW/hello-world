import requests
import urllib.request
import re
word=input("")
url = "https://image.baidu.com/search/index?tn=baiduimage&word="+word
header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3703.400 SLBrowser/10.0.3856.400'}
response =requests.get(url,headers=header)
response.encoding='utf-8'
a='"thumbURL":"(.*?)"'
#print(response.text)
data=re.compile(a).findall(response.text)
for i in range(len(data)):
    print(data[i])
    localfile="./"+str(i)+".jpg"
    print(localfile+"yixiazai")
    urllib.request.urlretrieve(data[i],filename=localfile)

