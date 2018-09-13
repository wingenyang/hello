# coding = utf-8

from bs4 import BeautifulSoup
import requests
import os

url = "http://699pic.com/nature.html"

r = requests.get(url)

html = r.content.decode("utf-8")

soup = BeautifulSoup(html,"html.parser")

imgs = soup.find_all(class_="lazy")

imgsPath = r"D:\imgs"
if not os.path.exists(imgsPath):
    os.mkdir(imgsPath)

for i in imgs:
    try:
        url = i["data-original"]
        name = i["title"]
        r1 = requests.get(url)
        fp = open(imgsPath+"\\%s.jpg" % name, "wb")
        fp.write(r1.content)
    except Exception as msg:
        print(msg)

fp.close()


