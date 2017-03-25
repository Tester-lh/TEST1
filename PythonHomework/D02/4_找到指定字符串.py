"""
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。
 如果不存在，则返回 -1。
"""
source='dasdlkmaflasmf'
target='sd123'
start=0
idx=source.find(target,start)
print(idx)