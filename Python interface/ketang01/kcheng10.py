# coding = utf-8

import requests

s = requests.session()
print(s.headers)
print("------------------------------------")
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
print(s.headers)

token = "123456789"

s.headers["token"] = token

print(s.headers)

url = "https://www.baidu.com"

r = s.get(url,verify=False)
