from random import sample
import openpyxl
from openpyxl.styles import Font, colors, fills

def generateXlsx(num):
    # 生成指定数量的Excel文件，并写入测试数据
    for i in range(num):
        # 新建Excel文件，获取第一个worksheet
        wb = openpyxl.Workbook()
        ws = wb.worksheets[0]
        # 添加表头
        ws.append(['字段'+str(_) for _ in range(1,6)])
        # 添加随机数据
        for _ in range(10):
            ws.append(sample(range(10000), 5))
        # 保持Excel文件
        wb.save(str(i)+'.xlsx')

def batchFormat(num):
    # 批量修改Excel文件的格式
    for i in range(num):
        # 打开指定的Excel文件，获取第一个worksheet
        fn = str(i)+'.xlsx'
        wb = openpyxl.load_workbook(fn)
        ws = wb.worksheets[0]
        # 枚举worksheet所有行
        for irow, row in enumerate(ws.rows, start=1):
            if irow == 1:
                # 表头加粗、黑体
                font = Font('黑体', bold=True)
            elif irow%2 == 0:
                # 偶数行红色，宋体
                font = Font('宋体', color=colors.RED)
            else:
                # 奇数行浅蓝色，宋体
                font = Font('宋体', color='00CCFF')
            for cell in row:
                # 设置该行所有单元格的字体
                cell.font = font
                # 偶数行添加背景填充色，从红到蓝渐变
                if irow%2 == 0:
                    cell.fill = fills.GradientFill(stop=['FF0000',
                                                             '0000FF'])
        # 另存为新文件
        wb.save('new'+fn)

generateXlsx(5)
batchFormat(5)
