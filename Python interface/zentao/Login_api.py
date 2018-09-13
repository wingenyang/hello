# coding = utf-8

import requests
from zentao.now_time import *


class Login_api():

    def __init__(self, s):
        self.s = s

    def login(self, username, pwd):
        url = "http://127.0.0.1/zentao/user-login.html"

        h = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        d = {
            "account": username,
            "password":	pwd,
            "referer": "http://127.0.0.1/zentao/my/"
        }

        r = self.s.post(url, headers=h, data=d)
        return r.content.decode("utf-8")

    def wj_shangchuan(self, pathname, imgspath):
        url = "http://127.0.0.1/zentao/file-ajaxUpload-5b91d9e1c4ec0.html"
        par = {
            "dir":"image"
        }
        # h = {
        #     "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryJiCBDiRSSbYrQUuW",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        # }
        f = {
            "localUrl":(None, pathname),
            "imgFile":(pathname, open(imgspath, "rb"), "image/jpeg")
        }

        r = self.s.post(url, params=par, files=f)
        try:
            imgUrl = r.json()
            return imgUrl
        except:
            return None

    def bd_tijiao(self, imgsname, imgspath):
        url = "http://127.0.0.1/zentao/bug-create-1-0-moduleID=0.html"
        d = {
            "product":"1",
            "module":"0",
            "project":"",
            "openedBuild[]":"trunk",
            "assignedTo":"admin",
            "type":"dedigndefect",
            "os":"win7",
            "browser":"",
            "color":"",
            "title":u"这是一个很奇葩的bug，这是一个很奇葩的bug%s"% nowtime,
            "severity":"3",
            "pri":"0",
            "steps":"<img src=\"data/upload/1/201809/07095317075181n.jpg\" "
                   "alt="" /><p>[步骤]1.打开浏览器</p><p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"
                   " 2.输入网址</p><p><br /></p>"
                   "<p>[结果]网址报404错误</p>"
                   "<p>[期望]能正常访问和登陆</p>",
            "task":"0",
            "story": "0",
            "mailto[]": "",
            "keywords": "",
            "uid": "5b91d9e1c4ec0",
            "case": "0",
            "caseVersion": "0",
            "result": "0",
            "testtask": "0"
        }
        f = [
            ["files[]",(imgsname,open(imgspath,"rb"),"image/png")],
        ]
        # h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        # }
        r = self.s.post(url,data=d,files=f)
        ret = r.content.decode("utf-8")
        return ret


if __name__ == "__main__":
    s = requests.session()
    z = Login_api(s)
    z.login("admin","123456")
    ret = z.wj_shangchuan("38.jpg","D:\\imgs\\38.jpg")
    print(ret)
    ret = z.bd_tijiao()
    print(ret)
