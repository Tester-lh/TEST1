# SuiteDemo.py


# -*- coding:utf-8 -*-


# 一个类，添加测试集


import unittest


class SuiteDemo(unittest.TestCase):
    # 测试用例前执行
    def setUp(self):
        print('Case Before')
        pass

    # 测试用例后执行
    def tearDown(self):
        print('Case After')
        pass

    def test_Case1(self):
        a = 3
        b = 2
        self.assertEqual(a + b, 5, 'Result Fail')
        print('Case1')

    def test_Case2(self):
        a = 2
        b = 3
        self.assertEqual(a * b, 6, 'Result Fail')
        print('Case2')


# 定义一个测试集合，方便添加Case

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(SuiteDemo("test_Case1"))
    suiteTest.addTest(SuiteDemo("test_Case2"))
    return suiteTest


# 默认运行时通过 Suite 运行

if __name__ == '__main__':
    unittest.main(defaultTest='suite')


sd = SuiteDemo()
rt= getattr(sd,'test_Case1')
print(rt())