#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql
import interfaceauto

CASE_ID = interfaceauto.CASE_ID
# CASE_ID = 2
try:
    # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='interfaceautotest', port=3306,
                           charset='utf8')
    # 获取一个用例
    cur = conn.cursor()
    cur.execute("SELECT * FROM `testcase` WHERE case_id= '%s' AND status=0" % CASE_ID)
    data = cur.fetchall()
    CASE_NAME = str(data[0][1]).strip()  # 用例名称
    REQUEST_URL = str(data[0][2]).strip()  # 请求地址
    REQUEST_METHOD = str(data[0][3]).strip()  # 请求方式
    cur.close()  # 关闭游标

    # 获取该用例参数
    cur = conn.cursor()
    cur.execute("SELECT * FROM `params` WHERE case_id= '%s'" % CASE_ID)
    data = cur.fetchall()
    PARAMS = {}
    for params in data:
        PARAMS_KEY = str(params[1]).strip()
        PARAMS_VALUES = str(params[2]).strip()
        PARAMS[PARAMS_KEY] = PARAMS_VALUES
        print(PARAMS)
    cur.close()  # 关闭游标

    conn.close()  # 释放数据库资源
except Exception as e:
    print('查询失败:', e)
