# coding = utf-8



import requests
from HRMS_test.api.Login_api import login

class Qj():
    host = "http://www.hrms.com"
    def __init__(self,s):
        self.token = login(s)

    def qj_sq(self,s,t="",s_time="",e_time="",r="",hname=""):

        url = self.host + "/api/leave/addApply"
        d = {
            "token": self.token,
            "type": t,
            "start": s_time,
            "end": e_time,
            "reason": r,
            "handover": hname
        }
        r = s.post(url,data=d)
        self.ret_msg = r.json()["ret_msg"]

        if r.json()["status"] == 0:
            self.sw = r.json()["sw"]
            self.eid = r.json()["e_id"]
            return self.sw, self.eid

        return self.ret_msg


    def qj_xg(self, s, t="", sx_time="", ex_time="", rx="",hxname=""):
        url = self.host + "/api/leave/editApply"
        d = {
            "token": self.token,
            "e_id": self.eid,
            "type": t,
            "start": sx_time,
            "end": ex_time,
            "reason": rx,
            "handover": hxname

        }
        r = s.post(url, data=d)
        return r.json()


if __name__ == "__main__":
    s = requests.session()
    q = Qj(s)
    res = q.qj_sq(s,t="5",s_time="2018-09-07 09:00",e_time="2018-09-07 12:00",r="我要请假了",hname="20")
    print(res)
    ret = q.qj_xg(s,t="5",sx_time="2018-09-07 12:00",ex_time="2018-09-07 18:00",rx="我要请假了,我要请假了",hxname="20")
    print(ret)

