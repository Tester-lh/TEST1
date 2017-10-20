# Test002_Fail.py


# -*- coding:utf-8 -*-

import unittest


class Test002_Fail(unittest.TestCase):
    # 测试用例前执行
    def setUp(self):
        print('Case Before')
        pass

    # 测试用例后执行
    def tearDown(self):
        print('Case After')
        pass

    # 测试用例1
    def test_Case1(self):
        a = 3
        b = 2
        self.assertEqual(a + b, 5, 'Result Fail')

    # 测试用例2
    def test_Case2(self):
        a = 2
        b = 3
        self.assertEqual(a * b, 7, 'Result Fail')


if __name__ == '__main__':
    unittest.main()
