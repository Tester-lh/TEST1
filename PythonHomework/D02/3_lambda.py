"""
实现函数fn(n)，返回一个函数f，f(x) = n * x。（利用lambda表达式）
"""


def fn(n):
    return lambda x: n * x

print(fn(5))
