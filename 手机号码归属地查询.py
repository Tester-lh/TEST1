#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, requests


# ----------------------------------
# 手机号码归属地调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/11
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "5e03120c28e7643b3de7d3015a1cf587"

    # 1.手机归属地查询
    getRequest(appkey, "GET")


# 手机归属地查询
def getRequest(appkey, method):
    url = "http://apis.juhe.cn/mobile/get"
    params = {
        "phone": "15980220341",  # 需要查询的手机号码或手机号码前7位
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json",  # 返回数据的格式,xml或json，默认json

    }
    f = requests.get(url, params)
    print( f.text )
    f.encoding = 'utf-8'
    # g = requests.post(url,data={"phone":"123123","asd":"12312"})
    # requests.get(‘https: // github.com / timeline.json’)  # GET请求
    # requests.post(“http: // httpbin.org / post”)  # POST请求
    # requests.put(“http: // httpbin.org / put”)  # PUT请求
    # requests.delete(“http: // httpbin.org / delete”)  # DELETE请求
    # requests.head(“http: // httpbin.org / get”)  # HEAD请求
    # requests.options(“http: // httpbin.org / get”)  # OPTIONS请求
    if method == "GET":
        f = requests.get(url, params)
        print(f.text)
    else:
        f = requests.get(url, params)
        print(f.text)
    res = json.loads(f.text)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
            print(res["result"]["province"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


if __name__ == '__main__':
    main()
