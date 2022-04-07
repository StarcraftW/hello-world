import requests
import re
url="http://www.lovehhy.net/ShiCi/Detail/"
ret=requests.get(url)
ret.encoding="gb2312"
print(ret.text)
pat='blank">(.*?)</a'
res=re.compile(pat,re.S).findall(ret.text)
for j in range(0,len(res)):
    print(str(res[j]))
