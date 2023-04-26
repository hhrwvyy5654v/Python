from string import digits
from itertools import combinations

for item in combinations(digits, 4):
    times = 0
    while True:
        # 当前选择的4个数字能够组成的最大数和最小数
        big = int(''.join(sorted(item, reverse=True)))
        little = int(''.join(sorted(item)))
        difference = big-little
        times = times+1
        # 如果最大数和最小数相减得到6174就退出
        # 否则就对得到的差重复这个操作
        # 最多7次，总能得到6174
        if difference==6174:
            if times>7:
                print(times)
            break
        else:
            item = str(difference)
