# 简化路径。给定一个文档(Unix-style)的完全路径，请进行路径简化。
# "/home/", => "/home“
# "/a/./b/../../c/", => "/c“

dir = "/a/./b/../../c/asd"


def simplify(d):
    l = d.split("/")
    if l[-1] == '':
        return '/' + l[-2]
    else:
        return '/' + l[-1]


print(simplify(dir))
