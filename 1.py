import requests
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
res=requests.get("https://www.baidu.com",headers=header)
print(res.encoding)#ISO-8859-1
print(res.request.headers)
res.encoding="utf-8"
print(res.text)
