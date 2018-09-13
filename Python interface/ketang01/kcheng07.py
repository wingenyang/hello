# coding = utf-8

import json

dict = {
    "a":123,
    "b":"123456",
    "c":True,
    "d":["a","b"]
    }

print(dict)
print(type(dict))
d_json = json.dumps(dict)
print(d_json)


d_dict = json.loads(d_json)
print(d_dict)