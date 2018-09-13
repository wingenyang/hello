# coding = utf-8

import requests

url = "https://passport.feng.com/index.php?r=user/LoginProcess&test=1"

# par = {
#     "r": "user/LoginProcess",
#     "test": 1
# }

# body = {
#     "username":	"bengen",
#     "password":	"bengen514",
#     "wekey_token": "",
#     "rememberMe": 0,
#     "feng_captcha":	"yJ4Ijo5OCwieSI6MTgxLjAwMDAzMDUxNzU3ODEyLCJ0aW1lIjoxMjc1LCJmaWxlIjoiMzg3ZWU1NDdkMmM5Y2U3NTY3OTc0YTNlN2MzNmMwZjUifQ%3D%3D"
# }

h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Referer":"https://passport.feng.com/?r=user/login&sso%5Bjump%5D=http%3A%2F%2Fbbs.feng.com%2Fhome.php%3Fmod%3Dspace%26uid%3D8323083&sso%5Bname%5D=%E5%A8%81%E9%94%8B%E8%AE%BA%E5%9D%9B&sso%5Bapps%5D=2&sso%5Bverify%5D=8cb4657d01a41d0f726655cfcffeec37",
    "Cookie": "UM_distinctid=165a24a2e840-049e1313c84247-37664109-510000-165a24a2e86a9e; username=bengen; PHPSESSID=564r535ufpr2pkcimd42tvke64; passport_user_info=eyJ1c2VybmFtZSI6ImJlbmdlbiJ9; SERVERID=104882b574c91d7c8db6fe3997326597|1536026207|1536026098"
}

r = requests.post(url, headers=h, verify=False)
print(r.text)