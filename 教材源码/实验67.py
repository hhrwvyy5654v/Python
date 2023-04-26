from hashlib import md5
from string import ascii_letters, digits
from itertools import permutations
from time import time

# 候选字符集
all_letters = ascii_letters + digits + '.,;'

def decrypt_md5(md5_value):
    # 破解32位MD5值
    if len(md5_value) != 32:
        print('error')
        return
    
    # 转换为小写MD5值
    md5_value = md5_value.lower()
    # 预期密码长度
    for k in range(5,10):
        # 暴力测试
        for item in permutations(all_letters, k): 
            item = ''.join(item)
            # 显示进度
            print('.', end='')
            if md5(item.encode()).hexdigest() == md5_value:
                return item

md5_value = 'b932ae9220e9a413b39d9782605fee8f'
start = time()
result = decrypt_md5(md5_value)
if result:
    print('\nSuccess:  '+md5_value+'==>'+result)
print('Time used:', time()-start)
