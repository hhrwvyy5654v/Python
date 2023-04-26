#（1）
num = input('请输入一个自然数：')
print(sum(map(int, num)))
#（2）
setA = eval(input('请输入一个集合：'))
setB = eval(input('再输入一个集合：'))
print('交集：', setA & setB)
print('并集：', setA | setB)
print('setA-setB：', setA - setB)
#（3）
num = int(input('请输入一个自然数：'))
print('二进制：', bin(num))
print('八进制：', oct(num))
print('十六进制：', hex(num))
#（4）
lst = input('请输入一个包含若干整数的列表：')
lst = eval(lst)
print(list(filter(lambda x: x%2==0, lst)))
#（5）
lstA = eval(input('请输入包含若干整数的列表lstA：'))
lstB = eval(input('请输入包含若干整数的列表lstB：'))
result = dict(zip(lstA, lstB))
print(result)
#（6)
lst = eval(input('请输入包含若干整数的列表lst：'))
print(sorted(lst, reverse=True))
#(7)
from functools import reduce
lst = eval(input('请输入包含若干整数的列表lst：'))
print(reduce(lambda x,y: x*y, lst))
#(8)
lstA = eval(input('请输入包含2个整数的列表lstA：'))
lstB = eval(input('请输入包含2个整数的列表lstB：'))
print(sum(map(lambda i,j:abs(i-j), lstA, lstB)))
#(9)
from functools import reduce
lstSets = eval(input('请输入包含若干集合的列表：'))
print(reduce(lambda x,y:x|y, lstSets))
#(10)
a1 = int(input('请输入等比数列首项：'))
q = int(input('请输入等比数列公比#（不等于1且小于36的正整数）：'))
n = int(input('请输入一个自然数：'))

result = a1 * int('1'*n, q)
print(result)
#(11)
data = input('请输入一个字符串：')
d = dict()
for ch in data:
    d[ch] = d.get(ch, 0) + 1
mostCommon = max(d.items(), key=lambda item:item[1])
print(mostCommon)
