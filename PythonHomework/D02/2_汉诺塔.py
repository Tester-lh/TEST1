"""
有三根杆子A，B，C。A杆上有N个(N>=1)穿孔圆盘，盘的尺寸由下到上依次变小。要求按下列规则将所有圆盘移至C杆：
每次只能移动一个圆盘；
大盘不能叠在小盘上面。
提示：可将圆盘临时置于B杆，也可将从A杆移出的圆盘重新移回A杆，但都必须遵循上述两条规则。
问：如何移？最少要移动多少次？
"""
step = 0


def move(n, a, buffer, c):
    global step
    if n < 1:
        return 0
    elif n == 1:
        print(a, "->", c)
        step += 1
        return 1
    move(n - 1, a, c, buffer)
    move(1, a, buffer, c)
    move(n - 1, buffer, a, c)


move(5, "a", "b", "c")
print(step)
