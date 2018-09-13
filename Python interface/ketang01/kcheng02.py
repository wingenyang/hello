# coding:utf-8

import requests

# 在只传输参数时打印的内容不正确时，就需要添加头部信息和cookies
url = "https://zzk.cnblogs.com/s/blogpost"
par = {
    "Keywords":"yoyoketang"
}
h = {
}

r = requests.get(url, params=par, headers=h)
print(r.text)