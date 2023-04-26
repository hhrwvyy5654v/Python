from itertools import combinations
from functools import reduce
import openpyxl
from openpyxl import Workbook

def getActors(filename):
    actors = dict()
    # 打开xlsx文件，并获取第一个worksheet
    wb = openpyxl.load_workbook(filename)
    ws = wb.worksheets[0]
    # 遍历Excel文件中的所有行
    for index, row in enumerate(ws.rows):
        # 绕过第一行的表头
        if index == 0:
            continue
        # 获取电影名称和演员列表
        filmName, actor = row[0].value, row[2].value.split('，')
        # 遍历该电影的所有演员，统计参演电影
        for a in actor:
            actors[a] = actors.get(a, set())
            actors[a].add(filmName)
    return actors

data = getActors('电影导演演员.xlsx')

def relations(num):
    # 参数num表示要查找关系最好的num个人    
    # 包含全部电影名称的集合
    allFilms = reduce(lambda x,y: x|y, data.values(), set())
    # 关系最好的num个演员及其参演电影名称
    combiData = combinations(data.items(), num)
    trueLove = max(combiData,
                   key=lambda item: len(reduce(lambda x,y:x&y,
                                           [i[1] for i in item],
                                           allFilms)))
    return ('关系最好的{0}个演员是{1}，'
            'Ta们共同主演的电影数量是{2}'.format(num,
                              tuple((item[0] for item in trueLove)),
                              len(reduce(lambda x,y:x&y,
                                     [item[1] for item in trueLove],
                                     allFilms))))

print(relations(2))
print(relations(3))
print(relations(4))
