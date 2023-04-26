while True:
    try:
        n = int(input('请输入评委人数：'))
        assert n>2
        break
    except:
        print('必须输入大于2的整数')
    
# 用来保存所有评委的打分
scores = []

# 依次输入每个评委的打分
for i in range(n):
    # 这个while循环用来保证用户必须输入0到100之间的数字
    while True:
        try:
            score = float(input('请输入第{0}个评委的分数：'.format(i+1)))
            assert 0<=score<=100
            scores.append(score)
            break
        except:
            print('必须属于0到100之间的实数.')

# 计算并删除最高分与最低分
highest = max(scores)
scores.remove(highest)
lowest = min(scores)
scores.remove(lowest)
# 计算平均分，保留2位小数
finalScore = round(sum(scores)/len(scores), 2)

formatter = '去掉一个最高分{0}\n去掉一个最低分{1}\n最后得分{2}'
print(formatter.format(highest, lowest, finalScore))
