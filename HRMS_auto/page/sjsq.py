# coding = utf-8

import requests
from common.re_token import get_token
host = "http://www.hrms.com"
def qj_sq(token,type="",start="",end="",reason="",handover=""):
    # token = get_token()
    url = host + "/api/leave/addApply"

    d = {
        "token": token,
        "type": type,
        "start": start,
        "end": end,
        "reason":reason,
        "handover":handover
    }
    r = requests.post(url, data=d)
    return r.json()["status"]

def bq_sq(token,ltype="",date="",type="",reason=""):
    url = host + "/api/signfix/addApply"
    d = {
        "token":token,
        "leak_type":ltype,
        "date": date,
        "type": type,
        "reason": reason
    }
    r = requests.post(url, data=d)
    return r.json()["status"]

if __name__ == "__main__":
    print(bq_sq("08b45763d74d32e9"))