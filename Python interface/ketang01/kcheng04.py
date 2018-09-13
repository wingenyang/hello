# coding:utf-8

import requests

s = requests.session()

url = "http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html"
body = {
    "referer": "/zentao/",
    "account": "admin",
    "password": "e10adc3949ba59abbe56e057f20f883e"

}
h ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
r = s.post(url, data=body, headers=h)
print(r.content.decode("utf-8"))

r1 = s.get("http://127.0.0.1:82/zentao/qa/", headers=h)
print(r1.content.decode("utf-8"))