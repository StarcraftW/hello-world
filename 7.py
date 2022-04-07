import re
import requests

url = 'http://www.heibanke.com/lesson/crawler_ex00/'
num = ""

while True:
    curl = url + num
    print(curl)
    r = requests.get(curl).text
    title = re.findall(r'数字(.*)</h3>', r)
    if title:
        title = "".join(title)
        print(title)
        num = re.findall("\d+", title)[0]
    else:
        break




