# 数组剔除元素后的乘积。给定一个整数数组A。
# 定义B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]， 计算B的时候请不要使用除法。
# 给出A=[1, 2, 3]，返回 B为[6, 3, 2]

def mul(a):
    b = []
    for i in range(0, len(a)):
        d = list(a)
        c = 1
        del d[i]
        for j in range(0, len(d)):
            c *= d[j]
        b.append(c)
    return b

A = [1, 2, 3]

print(mul(A))

#print([A[i]*A[x] for x in range(len(A)) if x!=i for i in range(len(A))])
#A[0]*a0*a1*a2
