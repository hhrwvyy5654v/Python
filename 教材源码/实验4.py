# 参考代码1：
maxNumber = int(input('请输入一个大于2的自然数：'))
lst = list(range(2, maxNumber))
# 最大整数的平方根
m = int(maxNumber**0.5)

for index, value in enumerate(lst):
    # 如果当前数字已大于最大整数的平方根，结束判断
    if value > m:
        break
    # 使用切片对该位置之后的元素进行过滤和替换
    lst[index+1:] = filter(lambda x: x%value != 0,
                             lst[index+1:])

print(lst)

# 参考代码2：
maxNumber = int(input('请输入一个大于2的自然数：'))
lst = list(range(2, maxNumber))
# 最大整数的平方根
m = int(maxNumber**0.5)

for index, value in enumerate(lst):
    if value > m:
        break
    for value1 in lst[:index:-1]:
        print(value1)
        if value1%value == 0:
            lst.remove(value1)

print(lst)
