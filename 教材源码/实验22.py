import random
import string

# 常用汉字Unicode编码表，可以自行搜索补充
StringBase = '\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba\u4eec'\
              '\u6709\u6765\u4ed6\u8fd9\u4e0a\u7740\u4e2a\u5730\u5230'\
              '\u5927\u91cc\u8bf4\u5c31\u53bb\u5b50\u5f97\u4e5f\u548c'\
              '\u90a3\u8981\u4e0b\u770b\u5929\u65f6\u8fc7\u51fa\u5c0f'\
              '\u4e48\u8d77\u4f60\u90fd\u628a\u597d\u8fd8\u591a\u6ca1'\
              '\u4e3a\u53c8\u53ef\u5bb6\u5b66\u53ea\u4ee5\u4e3b\u4f1a'\
              '\u6837\u5e74\u60f3\u751f\u540c\u8001\u4e2d\u5341\u4ece'\
              '\u81ea\u9762\u524d\u5934\u9053\u5b83\u540e\u7136\u8d70'\
              '\u5f88\u50cf\u89c1\u4e24\u7528\u5979\u56fd\u52a8\u8fdb'\
              '\u6210\u56de\u4ec0\u8fb9\u4f5c\u5bf9\u5f00\u800c\u5df1'\
              '\u4e9b\u73b0\u5c71\u6c11\u5019\u7ecf\u53d1\u5de5\u5411'\
              '\u4e8b\u547d\u7ed9\u957f\u6c34\u51e0\u4e49\u4e09\u58f0'\
              '\u4e8e\u9ad8\u624b\u77e5\u7406\u773c\u5fd7\u70b9\u5fc3'\
              '\u6218\u4e8c\u95ee\u4f46\u8eab\u65b9\u5b9e\u5403\u505a'\
              '\u53eb\u5f53\u4f4f\u542c\u9769\u6253\u5462\u771f\u5168'\
              '\u624d\u56db\u5df2\u6240\u654c\u4e4b\u6700\u5149\u4ea7'\
              '\u60c5\u8def\u5206\u603b\u6761\u767d\u8bdd\u4e1c\u5e2d'
def getEmail():
    # 常见域名后缀，可以随意扩展该列表
    suffix = ['.com', '.org', '.net', '.cn']
    characters = string.ascii_letters+string.digits+'_'
    username = ''.join((random.choice(characters)
                          for i in range(random.randint(6,12))))
    domain = ''.join((random.choice(characters)
                        for i in range(random.randint(3,6))))
    return username+'@'+domain+random.choice(suffix)

def getTelNo():
    return ''.join((str(random.randint(0,9))
                      for i in range(11)))

def getNameOrAddress(flag):
    '''flag=1表示返回随机姓名，flag=0表示返回随机地址'''
    result = ''
    if flag==1:
        # 大部分中国人姓名在2-4个汉字
        rangestart, rangeend = 2, 5
    elif flag==0:
        # 假设地址在10-30个汉字之间
        rangestart, rangeend = 10, 31
    else:
        print('flag must be 1 or 0')
        return ''
    # 生成并返回随机信息
    for i in range(random.randrange(rangestart, rangeend)):
        result += random.choice(StringBase)
    return result

def getSex():
    return random.choice(('男', '女'))

def getAge():
    return str(random.randint(18,100))

def main(filename):
    with open(filename, 'w', encoding='utf-8') as fp:
        # 写入表头
        fp.write('Name,Sex,Age,TelNO,Address,Email\n')
        # 生成200个人的随机信息
        for i in range(200):
            name = getNameOrAddress(1)
            sex = getSex()
            age = getAge()
            tel = getTelNo()
            address = getNameOrAddress(0)
            email = getEmail()
            line = ','.join([name,sex,age,tel,address,email])+'\n'
            fp.write(line)
            
def output(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        for line in fp:
            print(line)
            
if __name__ == '__main__':
    filename = 'information.txt'
    main(filename)
    output(filename)
