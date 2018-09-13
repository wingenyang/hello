# coding= utf-8

import requests
import urllib3
urllib3.disable_warnings()

s = requests.session()

url = "https://weibo.com/aj/mblog/add"
par = {
    "ajwvr":6,
    "__rnd":"1536045973186"
   }

body = {
    "_t":	0,
    "appkey": "",
    "isPri": 0,
    "isReEdit":	"false",
    "location":	"v6_content_home",
    "mid": "",
    "module": "stissue",
    "pdetail": "",
    "pic_id":	"",
    "pub_source": "main_",
    "pub_type":	"dialog",
    "rank":	0,
    "rankid":	"",
    "style_type": 1,
    "text":	"在家待业好长时间了,很无聊。。。",
    "tid": ""
}

h = {   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
}
r = s.post(url,params=par,data=body,headers=h,verify=False)


c = requests.cookies.RequestCookieJar()
c.set("SUBP", "0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh4ALmx1i9HBwzSoRZ7SXoe5JpX5K2hUgL.Foz0So5RSh2E1h-2dJLoI0zLxK-LBKBLBKMLxK-L1hzLB.zLxKBLBonL12BLxKqL1KnLB-qLxKqL1-BLBKyjwgLDIBtt")
c.set("ALF", "1567581922")
c.set("SSOLoginState", "1536045923")
c.set("SCF", "AuhkWRNMakXk6kYsOysI7UHpIuVe7F-3Sn_Zx6L0JYqLypnngQV7JxpL_igYTjrFDxDHZku44FDTAJ3OHuCd2F8")
c.set("SUB", "_2A252ikMzDeRhGeRN7VIZ9C_OwzmIHXVV_jP7rDV8PUNbmtBeLW39kW9NU5nF2joU1Sc9RCYA6n7FQ8hseyevytNZ")
c.set("SUHB", "0ftYOZx6Wde7hS")
c.set("un", "13510117947")
c.set("wvr", "6")
c.set("YF-Page-G0", "86b4280420ced6d22f1c1e4dc25fe846")
c.set("wb_view_log_2360841285", "3072*17281.25")
c.set("wb_timefeed_2360841285", "1")

c.cookies.update(c)

r1 = s.post(url,params=par,data=body,headers=h,verify=False)
print(r1.content.decode("gbk"))


