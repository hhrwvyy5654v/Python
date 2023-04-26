import tkinter
from PIL import ImageGrab, ImageTk

# 创建应用程序主窗口，铺满整个屏幕，并删除标题栏
root = tkinter.Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry(str(screenWidth)+'x'+str(screenHeight)+'+0+0')
root.overrideredirect(True)
# 不允许改变窗口大小
root.resizable(False, False)
# 创建画布，显示全屏截图，以便后面在全屏截图上进行区域截图并进行放大
canvas = tkinter.Canvas(root, bg='white',
                          width=screenWidth,
                          height=screenHeight)
image = ImageTk.PhotoImage(ImageGrab.grab())
canvas.create_image(screenWidth//2, screenHeight//2,
                      image=image)

# 右键退出桌面放大器程序
def onMouseRightClick(event):
    root.destroy()
canvas.bind('<Button-3>', onMouseRightClick)

# 截图窗口半径
radius = 20
def onMouseMove(event):
    global lastIm, subIm
    try:
        canvas.delete(lastIm)
    except:
        pass
    # 获取鼠标位置
    x = event.x
    y = event.y
    # 二次截图，放大3倍，在鼠标当前位置左上方显示
    subIm = ImageGrab.grab((x-radius, y-radius,
                              x+radius, y+radius))
    subIm = subIm.resize((radius*6, radius*6))
    subIm = ImageTk.PhotoImage(subIm)
    lastIm = canvas.create_image(x-70, y-70, image=subIm)
    # canvas.update()
# 绑定鼠标移动事件处理函数
canvas.bind('<Motion>', onMouseMove)

# 把画布对象canvas放置到窗体上
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        
# 启动消息主循环
root.mainloop()
