def Rate(origin, userInput):
    if not (isinstance(origin, str)
             and isinstance(userInput, str)):
        return 'The two parameters must be strings.'
    if len(origin)<len(userInput):
        return 'Sorry. I suppose the second string is shorter.'

    # 精确匹配的字符个数
    right = sum(1
                 for oc, uc in zip(origin, userInput)
                 if oc==uc)
    return right/len(origin)

# 测试数据
origin = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.'''
userInput = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
readability counts.'''

# 测试函数功能
print(round(Rate(origin, userInput)*100, 2), '%', sep='')
