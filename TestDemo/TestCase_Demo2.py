# TestCase_Demo2.py


# -*- coding:utf-8 -*-


#集合可以写在main


import unittest
from TestCase_Demo import TestCaseDemo


#指定并启动测试集合

if __name__ == '__main__':

    #添加测试集合Case,并启动
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo('test_Case1'))
    suiteTest.addTest(TestCaseDemo('test_Case2'))

    #直接启动集合
    runner = unittest.TextTestRunner()
    runner.run(suiteTest)