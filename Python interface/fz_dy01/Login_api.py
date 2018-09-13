# coding:utf-8


import requests
import urllib3
urllib3.disable_warnings()

class Login():
    host = "http://www.hrms.com"
    s = requests.session()
    def login(self,username,pwd):
        url = self.host +"/api/doLogin"
        data = {
            "username":username,
            "password":pwd
        }
        r = self.s.post(url,data=data)
        self.token = r.json()["token"]
        return self.token

    def sj_qj(self,s_time="", e_time="", reason="", h_name=""):
        url = "http://www.hrms.com/api/leave/addApply"
        d = {
            "token":self.token,
            "type":"5",
            "start":s_time,
            "end":e_time,
            "reason":reason,
            "handover":h_name}
        r = self.s.post(url, data=d)
        self.sw = r.json()["sw"]
        self.eid = r.json()["e_id"]
        # self.ret = (self.sw,self.eid)
        # print(self.ret[0])
        return self.sw,self.eid


    def shantie(self):
        url = self.host + "/api/deleteApply"
        par = {
            "token":self.token,
            "e_id":self.eid,
            "type":self.sw
        }
        r = self.s.get(url, params=par)
        return r.json()

if __name__ == "__main__":
    blog = Login()
    blog.login("15673200007", "123456")
    ret = blog.sj_qj(s_time="2018/09/06 09:00",e_time="2018/09/07 12:00",reason=u"请婚假回家摆酒",h_name="20")
    print(ret)
    res = blog.shantie()
    print(res)

