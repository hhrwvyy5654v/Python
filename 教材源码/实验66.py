from string import ascii_uppercase as uppercase
from itertools import cycle

# 加密置换表
table = dict()
for index, ch in enumerate(uppercase):
    table[ch] = uppercase[index:]+uppercase[:index]


deTable = {'A':'A'}
start = 'Z'
for index, ch in enumerate(uppercase[1:], start=1):
    deTable[ch] = chr(ord(start)+1-index)

def deKey(key):
    # 根据加密密钥，计算解密密钥
    return ''.join([deTable[i] for i in key])

#加密/解密
def encrypt(plainText, key):
    result = []
    # 创建cycle对象，支持密钥字母的循环使用
    currentKey = cycle(key)
    for ch in plainText:
        # 逐个处理文本中的每个字符
        if 'A'<=ch<='Z':
            index = uppercase.index(ch)
            # 获取密钥字母
            ck = next(currentKey)
            # 获取置换结果字母
            result.append(table[ck][index])
        else:
            result.append(ch)
    return ''.join(result)

key = 'DONGFUGUO'
p = 'PYTHON 3.6.5 PYTHON 3.7'
c = encrypt(p, key)
print('初始明文：', p)
print('加密结果：', c)
print('解密结果：', encrypt(c,deKey(key)))
