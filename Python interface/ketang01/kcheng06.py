# coding = utf-8

import requests

s = requests.session()

loginUrl = "http://www.hrms.com/system/login_check"

data = {
    "_password":"123456",
    "_username":"15673200007"
}

h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
     "Content-Type": "application/x-www-form-urlencoded",
     "Cookie":"PHPSESSID=d6c14kkhkn6fifks0j1pakt9ha"


}

# r = s.post(url=loginUrl, data=data, headers=h)
#
# c = requests.cookies.RequestsCookieJar()
# c.set("PHPSESSID","d6c14kkhkn6fifks0j1pakt9ha")
# r.cookies.update(c)
#
# r2 = s.post(url=loginUrl, cookies=c)
# print(r2.text)
# print(r.text)
r = s.post(url=loginUrl,data=data,headers=h)
print(r.text)
print(r.cookies)
