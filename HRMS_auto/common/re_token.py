# coding = utf-8

import yaml
import os

# 获取项目真实路径
cur = os.path.dirname(os.path.realpath(__file__))

def get_token(yamlName="token.yaml"):

    '''
    从token.yaml读取token值
    param yamlName：配置文件名称
    return： 返回token值
    '''
    p = os.path.join(cur, yamlName)
    f = open(p)
    a = f.read()

    # 导入
    t = yaml.load(a)
    f.close()
    return t["token"]

if __name__ == "__main__":
    print(get_token())