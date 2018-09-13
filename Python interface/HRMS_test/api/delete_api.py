# coding =utf-8

import requests
from HRMS_test.api.Login_api import login
from HRMS_test.api.qj_sq_xg_api import *
import time

def delete(s):
    t = Qj(s)
    ts = t.qj_sq(s,t="10",s_time="2018-09-07 09:00",e_time="2018-09-07 12:00",r="我要请假，删除此次请假",hname="20")
    token = login(s)
    print(ts)

    time.sleep(20)
    url = "http://www.hrms.com/api/deleteApply"
    par = {
        "token":token,
        "e_id":ts[1],
        "type":ts[0]
    }
    r = s.get(url,params=par)
    return r.json()

if __name__ == "__main__":
    s = requests.session()
    t = delete(s)
    print(t)
