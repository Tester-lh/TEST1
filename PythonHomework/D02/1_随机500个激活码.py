import random

str1 = ''
for j in range(0, 100):
    for i in range(0, 4):
        str1 += random.choice([str(random.randint(0, 9)), chr(random.randint(65, 90))])
        i += 1
    str1 += '-'
    j += 1
# rstrip删除最右指定字符，为空默认删除空白符（包括'\n','\r','\t',' ')，最左lstrip,两端直接strip
print(str1.rstrip('-'))

# 法二append和join的使用
str2 = ''
list2 = []
for j in range(0, 100):
    for i in range(0, 4):
        str2 += random.choice([str(random.randint(0, 9)), chr(random.randint(65, 90))])
        i += 1
    list2.append(str2)
    j += 1
    str2 = ''
print('-'.join(list2))

# 法三
str3 = ''
for i in range(0, 500):
    str3 += random.choice([str(random.randint(0, 9)), chr(random.randint(65, 90))])
    if ((i + 1) % 4 == 0) & (i != 499):
        str3 += '-'
print(str3)
