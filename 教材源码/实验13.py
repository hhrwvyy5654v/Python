from random import randrange

def playGame():
    value = randrange(360)
    # 查找并返回本次获奖情况
    for k, v in areas.items():
        if v[0]<=value<v[1]:
            return k
        
# 各奖项对应面积在轮盘上所占比例
areas = {'一等奖':(0, 30),
         '二等奖':(30, 108),
         '三等奖':(108, 360)}

# 记录每个奖项的获奖次数
results = dict()

for i in range(10000):
    r = playGame()
    results[r] = results.get(r, 0) + 1

for item in results.items():
    print('{0[0]}：{0[1]}次'.format(item))
