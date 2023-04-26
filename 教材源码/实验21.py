def check(text, rate=0.2):
    characters = '【】*-/\\'
    num = sum(map(
        lambda ch:text.count(ch),
        characters))
    if num/len(text) > rate:
        return '垃圾邮件'
    return '正常邮件'

# 测试函数功能
text = '我公【司免】费开发【票，微*信*同-号'
print(check(text))
print(check(text, 0.5))
