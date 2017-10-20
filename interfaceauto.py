#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, requests, pymysql
import getSource

CASE_ID = 3


def main():
    if getSource.REQUEST_METHOD == "GET":
        getRequest()
    elif getSource.REQUEST_METHOD == "POST":
        postRequest()


# GET请求
def getRequest():
    f = requests.get(getSource.REQUEST_URL, getSource.PARAMS)
    print(f.url)
    print(f.text)
    f.encoding = 'utf-8'
    check(f)


# POST请求
def postRequest():
    f = requests.post(getSource.REQUEST_URL, getSource.PARAMS)
    print(f.url)
    print(f.text)
    f.encoding = 'utf-8'
    check(f)


def check(f):
    flag = 0
    res = json.loads(f.text)
    keys = list(res.keys())
    print(keys)
    for key in keys:
        if isinstance(res[key], dict):  # 判断类型是否匹配，若为字典则还有值

            # 获取该用例断言
            if res[key] == {}:  # 判断为空的字典是否在校验范围，若数据库存在对这个父节点相关校验，则报错
                conn2 = pymysql.connect(host='localhost', user='root', passwd='root', db='interfaceautotest', port=3306,
                                        charset='utf8')
                cur2 = conn2.cursor()
                cur2.execute(
                    "SELECT count(*) FROM `checkpoint` WHERE case_id='%s' and point_name= '%s' " % (CASE_ID, key))
                data2 = cur2.fetchall()
                cur2.close()  # 关闭游标
                if data2[0][0] != 0:
                    flag = 1
                    print(key + "   flase")
            else:
                for key2 in list(res[key].keys()):  # 判断非空的字典中的校验点进行匹配判断
                    try:
                        conn2 = pymysql.connect(host='localhost', user='root', passwd='root', db='interfaceautotest',
                                                port=3306,
                                                charset='utf8')
                        cur2 = conn2.cursor()
                        cur2.execute(
                            "SELECT point_values FROM `checkpoint` WHERE case_id= '%s' AND point_name='%s' AND parent_id=(SELECT point_id FROM checkpoint WHERE point_name = '%s')" % (
                                CASE_ID, key2, key))
                        data2 = cur2.fetchall()
                        POINT_VALUES = data2[0][0]
                        cur2.close()  # 关闭游标
                        if str(POINT_VALUES) == str(res[key][key2]):
                            print(key + '.' + key2 + '  pass')
                        else:
                            flag = 1
                            print(key2 + "   flase")
                    except Exception:
                        print('此用例中不对' + key + "下的" + key2 + '项进行比对;')
        else:
            # 获取该用例断言
            try:
                conn2 = pymysql.connect(host='localhost', user='root', passwd='root', db='interfaceautotest', port=3306,
                                        charset='utf8')
                cur2 = conn2.cursor()
                cur2.execute(
                    "SELECT point_values FROM `checkpoint` WHERE case_id='%s' and point_name= '%s' " % (CASE_ID, key))
                data2 = cur2.fetchall()
                POINT_VALUES = data2[0][0]
                cur2.close()  # 关闭游标
                if str(POINT_VALUES) == str(res[key]):
                    print(key + "  pass")
                else:
                    flag = 1
                    print(key + "flase")
            except Exception:
                print('此用例中不对' + key + '项进行比对;')
    conn2.close()  # 释放数据库资源
    if flag == 0:
        print("-------------------------")
        print("     用例执行成功")
        print("-------------------------")
    else:
        print("-------------------------")
        print("     用例执行失败")
        print("-------------------------")


if __name__ == '__main__':
    main()
