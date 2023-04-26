maxNumber = int(input('请输入一个大于2的自然数：'))
numbers = set(range(2, maxNumber))

# 最大数的平方根，以及小于该数字的所有素数
m = int(maxNumber**0.5)+1
primesLessThanM = [p for p in range(2, m)
                     if 0 not in [p%d
                                   for d in range(2,int(p**0.5)+1)]]

# 遍历最大整数平方根之内的自然数
for p in primesLessThanM:
    for i in range(2, maxNumber//p+1):
        # 在集合中删除该数字所有的倍数
        numbers.discard(i*p)
        
print(numbers)
