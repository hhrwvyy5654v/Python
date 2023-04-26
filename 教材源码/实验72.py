import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

def circleXY(r=20, sideNum=6):
    theta = np.linspace(0, 2*np.pi,# 绘制一个完整的圆
                          sideNum,   # 边的数量
                          False)     # 划分角度时不包含终点
    x = r*np.sin(theta)            # 圆周上点的x坐标
    x = np.append(x, x[0])         # 首尾相连
    y = r*np.cos(theta)            # 圆周上点的y坐标
    y = np.append(y, y[0])         # 首尾相连
    return (x,y)

fig, ax = plt.subplots()           # 创建图形和轴
plt.subplots_adjust(left=0.1,      # 调整绘制结果图形的位置
                      bottom=0.25)

x, y = circleXY()
l, = plt.plot(x, y,                # 绘制折线图，正多边形
               lw=2, color='red')   # 设置线宽和颜色

axColor = 'lightgoldenrodyellow'
# 创建Slider组件，设置位置/尺寸、背景色和初始值
axSideNum = plt.axes([0.2, 0.1, 0.6, 0.03], # Slider左上角位置和大小
                       facecolor=axColor) 
slideSideNum = Slider(axSideNum, 'side number',
                        valmin=3, valmax=60,  # 最小值、最大值
                        valinit=6,             # 默认值
                        valfmt='%d')           # 数字显示格式

# 为Slider组件设置事件处理函数
def update(event):
    sideNum = int(slideSideNum.val)          # 获取Slider组件的当前值
    x, y = circleXY(sideNum=sideNum)         # 重新计算圆周上点的坐标
    l.set_data(x, y)                          # 更新数据
    plt.draw()                                 # 重新绘制多边形
slideSideNum.on_changed(update)

# 创建按钮组件，用来恢复Slider组件的初始值
resetax = plt.axes([0.45, 0.03, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axColor, hovercolor='yellow')
def reset(event):
    slideSideNum.reset()
button.on_clicked(reset)

ax.set_aspect('equal')      # 设置坐标轴纵横比相等
ax.set_xlim(-22, 22)        # 设置x轴刻度起止值
ax.set_ylim(-22, 22)

plt.show()                   # 显示图形
