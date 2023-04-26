from math import log2
from random import randint, choice

def everyStep(n):
    half = n / 2
    m = 1
    # 所有可能满足条件的取法
    possible = []
    while True:
        rest = 2**m - 1
        if rest >= n:
            break
        if rest >= half:
            possible.append(n-rest)
        m = m+1
    # 如果至少存在一种取法使得剩余物品数量为2^n-1
    if possible:
        return choice(possible)
    # 无法使得剩余物品数量为2^n-1，随机取走一些
    return randint(1, int(half))

def smartNimuGame(n):
    while n > 1:
        # 人类玩家先走
        print("It's your turn, and we have {0} left.".format(n))
        # 确保人类玩家输入合法整数值
        while True:
            try:
                num = int(input('How many do you want to take:'))
                assert 1 <= num <= n//2
                break
            except:
                print('Must be between 1 and {0}'.format(n//2))
        n -= num
        if n == 1:
            return 'I fail.'
        # 计算机玩家拿走一些
        n -= everyStep(n)            
    else:
        return 'You fail.'

print(smartNimuGame(randint(1, 100)))
