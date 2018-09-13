# coding = utf-8

import requests
import json

url = "http://japi.juhe.cn/qqevaluate/qq"

par  = {
    "key": "8dbee1fcd8627fb6699bce7b986adc45",
    "qq": "593383513"
}

r = requests.get(url, params=par)
# print(r.text) # 返回的时json数据

# print(json.loads(r.text))
# print(type(json.loads(r.text)))

# 最简单的json转换成dict
# list和tuple都是用下标进行获取值
res = r.json()
print(res)
print(res["reason"])
print(res["result"]["data"]["analysis"])