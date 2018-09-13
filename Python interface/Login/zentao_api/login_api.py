# coding = utf-8

import requests

def login(s, username, password):

    url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
    body = {
        "referer": "/zentao/",
        "account": username,
        "password": password
    }
    h ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"

    }
    r = s.post(url, data=body, headers=h)
    return r.content.decode("utf-8")

if __name__ == "__main__":
    s = requests.session()
    ret = login(s,"admin", "e10adc3949ba59abbe56e057f20f883e")
    print(ret)
