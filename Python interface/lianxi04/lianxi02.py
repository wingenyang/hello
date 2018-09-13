# coding = utf-8

import requests
from requests.cookies import RequestsCookieJar
s = requests.session()
url = "http://www.hrms.com/login"
url1 = "http://www.hrms.com/system/staff/signin/addaction"

body = {
    "type":1,
    "reason":"testtesttesttesttest",
    "leak_clock_type":1,
    "date":"2018/09/04 09:00"
}

h = {
    # "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

}

r = s.post(url,headers=h)
# print(r.text)


c = RequestsCookieJar()
c.set("PHPSESSID","7tqcuiuiljnmbnj2b4t95ckt8g")


r1 = s.post(url=url1,data=body,headers=h,cookies=c)
print(r1.text)