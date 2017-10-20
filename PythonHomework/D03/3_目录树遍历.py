# 目录树遍历（os.listdir获得文件列表，os.path.isdir判断是否目录）
import os

dire = 'C:\\Users\\Administrator\\Desktop\\test123'
lon = len(dire.split('\\'))


def dirBianli(dir):
    li = os.listdir(dir)
    global lon
    for i in range(0, len(li)):
        if os.path.isdir(dir + '\\' + li[i]):
            print('|' * (len(dir.split('\\')) - lon) + '|-' + li[i])
            dir2 = dir + '\\' + li[i]
            dirBianli(dir2)
        else:
            print('|' * (len(dir.split('\\')) - lon) + '|-' + li[i])

def treedir(dir):
    li = os.listdir(dir)

    return

dirBianli(dire)
