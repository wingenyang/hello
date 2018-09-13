# coding:utf-8

import requests
import urllib3
urllib3.disable_warnings()  # 忽略警告

url = "https://www.baidu.com"

r = requests.get(url)
print(r.text)  # 文本格式打印出来有乱码，那就以字节的方式输出

# 用content输出，就不会有乱码了,但是输出的时ascii码，所以需要解码成utf-8
print(r.content.decode("utf-8"))
print(r.encoding)  # 返回页面的编码格式
print(r.url)


# 需要打开抓包工具，同时也要运行脚本，则在requests，get（）中添加一个参数：verify=False

