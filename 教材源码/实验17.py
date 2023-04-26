def hannoi(num, src, dst, temp=None):  #递归算法
    if num < 1:
        return

    global times    #声明用来记录移动次数的变量为全局变量
    # 递归调用函数自身，先把除最后一个盘子之外的所有盘子移动到临时柱子上
    hannoi(num-1, src, temp, dst)
    # 移动最后一个盘子
    print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
    towers[dst].append(towers[src].pop())
    for tower in 'ABC':    #输出3根柱子上的盘子
        print(tower, ':', towers[tower])
    times += 1
    # 把除最后一个盘子之外的其他盘子从临时柱子上移动到目标柱子上
    hannoi(num-1, temp, dst, src)

#用来记录移动次数的变量
times = 1
# 盘子数量
n = 64
towers = {'A':list(range(n, 0, -1)), #初始状态，所有盘子都在A柱上
           'B':[],
           'C':[]
          }
# A表示最初放置盘子的柱子，C是目标柱子，B是临时柱子
hannoi(n, 'A', 'C', 'B')
