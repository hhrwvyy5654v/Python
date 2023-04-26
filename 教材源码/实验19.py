import string
def kaisa(s, k):
	lower = string.ascii_lowercase        #小写字母
	upper = string.ascii_uppercase        #大写字母
	before = string.ascii_letters
	after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
	table = ''.maketrans(before, after)   #创建映射表
	return s.translate(table)              #返回加密结果

s = input('请输入一个字符串：')
k = int(input('请输入一个整数密钥：'))
print(kaisa(s, k))
