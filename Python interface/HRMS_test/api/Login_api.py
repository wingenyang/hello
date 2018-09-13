# coding = utf-8

import requests

def login(s,username="15673200007",pwd="123456"):
    url = "http://www.hrms.com/api/doLogin"
    d = {
        "username":username,
        "password":pwd
    }

    r = s.post(url, data=d)
    token = r.json()["token"]
    return token


if __name__ == "__main__":
    s = requests.session()
    l = login(s)
    print(l)