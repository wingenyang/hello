# coding = utf-8

import requests
from urllib import parse

url = "http://zzk.cnblogs.com/s/blogpost?Keywords=中文"

r = requests.get(url)
print(r.url)
res = r.url
res = res.split("?")[1]
res = res.split("=")[1]
print(res)

# 导入urllib中的parse，使用parse.unquote()进行解码
res = parse.unquote(res)
print(res)

# 编码只建议对中文进行编码和解码
a = "中文"
print(parse.quote(a))

import re

# 正则 ：末尾没有参数时：r"(.+?)$"；末尾还有参数:r"(.+?)&"