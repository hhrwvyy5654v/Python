#参考代码1（使用标准库itertools）：
from itertools import cycle

def demo(lst, k):
    # 切片，以免影响原来的数据
    t_lst = lst[:]
    
    # 游戏一直进行到只剩下最后一个人
    while len(t_lst) > 1:
        print(t_lst)
        # 创建cycle对象
        c = cycle(t_lst)
        # 从1到k报数
        for i in range(k):
            t = next(c)
        # 一个人出局，圈子缩小
        index = t_lst.index(t)
        t_lst = t_lst[index+1:] + t_lst[:index]
        
    # 游戏结束
    return t_lst[0]

lst = list(range(1,11))
print(demo(lst, 3))

#参考代码2（使用列表方法）：
def demo(lst, k):
    # 切片，以免影响原来的数据
    t_lst = lst[:]
    
    # 游戏一直进行到只剩下最后一个人
    while len(t_lst) > 1:
        print(t_lst)
        # 模拟报数
        for i in range(k-1):
            t_lst.append(t_lst.pop(0))
        t_lst.pop(0)
        
    # 游戏结束
    return t_lst[0]

lst = list(range(1, 11))
print(demo(lst, 3))
