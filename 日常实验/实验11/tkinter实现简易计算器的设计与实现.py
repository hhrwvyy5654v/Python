# encoding: utf-8
from tkinter import *


class Application(Frame):  # 继承Frame类
    def __init__(self, master=None, **kw):
        super().__init__(master=None, **kw)  # 继承父类的初始化方法
        self.master = master
        self.memory_state = StringVar()  # 设定第一部分'记忆'状态变量
        self.memory_value = ''  # 设定记忆存储的数值，初始状态为空
        self.input_value = StringVar()  # 设定第二部分存储输入值的变量
        self.output_value = StringVar()  # 设定第三部分存储计算结果变量
        self.button_list = []
        self.key_value_list = []
        self.bind("<Key>", self.key_display)
        self.focus_set()
        self.pack()  # 将实例布局到窗口
        self.create_widgets()  # 调用控件布局函数

    # 定义创建控件函数
    def create_widgets(self):
        # 设置第一部分'记忆'状态显示控件, 把状态变量赋值给textvariable
        label_memory = Label(self, textvariable=self.memory_state)
        label_memory.grid(row=0, column=0, pady=2)  # 把控件布局到第一行,第一列注意行列的坐标从0开始
        entry = Entry(self, textvariable=self.input_value,
                      justify=RIGHT)  # 设置第二部分控件输入值显示窗口
        entry.grid(row=1, column=0, columnspan=4,
                   sticky=EW, pady=2)  # 布局输入值显示窗口到第二整行
        # 设置第三部分控件计算结果显示窗口
        label_output = Label(self, textvariable=self.output_value, anchor=E)
        label_output.grid(row=2, column=0, columnspan=4,
                          sticky=EW, pady=2)  # 布局输出值显示到第三整行

        # 生成按键布局
        keys_tuples = (("MC", "M+", "M-", 'MR'), ("C", "x", "÷", "⬅"), ("7", "8", "9", "-"),
                       ("4", "5", "6", "+"), ("1", "2", "3", "="), ("%", "0", "."))  # 将按键列表按行存储到元组中

        for index_row, keys_tuple in enumerate(keys_tuples):  # 遍历行索引及按键行元组
            for index_column, key in enumerate(keys_tuple):  # 遍历列索引及单个按键
                if key == '=':  # 当按键为'='时合并两列
                    button = Button(self, text=key, width=2)
                    button.grid(row=index_row + 3, column=index_column,
                                rowspan=2, sticky=NS, pady=2)
                else:
                    button = Button(self, text=key, width=2)  # 生成单个按键控件
                    button.grid(row=index_row+3, column=index_column,
                                pady=2)  # 布局单个按键到相应位置
                self.button_list.append(button)  # 添加控件到控件列表
                self.key_value_list.append(key)  # 添加按键值到按键列表

        # 对应按键及对应数值 共计23对
        self.button_list[0].config(
            command=lambda: self.display(self.key_value_list[0]))
        self.button_list[1].config(
            command=lambda: self.display(self.key_value_list[1]))
        self.button_list[2].config(
            command=lambda: self.display(self.key_value_list[2]))
        self.button_list[3].config(
            command=lambda: self.display(self.key_value_list[3]))
        self.button_list[4].config(
            command=lambda: self.display(self.key_value_list[4]))
        self.button_list[5].config(
            command=lambda: self.display(self.key_value_list[5]))
        self.button_list[6].config(
            command=lambda: self.display(self.key_value_list[6]))
        self.button_list[7].config(
            command=lambda: self.display(self.key_value_list[7]))
        self.button_list[8].config(
            command=lambda: self.display(self.key_value_list[8]))
        self.button_list[9].config(
            command=lambda: self.display(self.key_value_list[9]))
        self.button_list[10].config(
            command=lambda: self.display(self.key_value_list[10]))
        self.button_list[11].config(
            command=lambda: self.display(self.key_value_list[11]))
        self.button_list[12].config(
            command=lambda: self.display(self.key_value_list[12]))
        self.button_list[13].config(
            command=lambda: self.display(self.key_value_list[13]))
        self.button_list[14].config(
            command=lambda: self.display(self.key_value_list[14]))
        self.button_list[15].config(
            command=lambda: self.display(self.key_value_list[15]))
        self.button_list[16].config(
            command=lambda: self.display(self.key_value_list[16]))
        self.button_list[17].config(
            command=lambda: self.display(self.key_value_list[17]))
        self.button_list[18].config(
            command=lambda: self.display(self.key_value_list[18]))
        self.button_list[19].config(
            command=lambda: self.display(self.key_value_list[19]))
        self.button_list[20].config(
            command=lambda: self.display(self.key_value_list[20]))
        self.button_list[21].config(
            command=lambda: self.display(self.key_value_list[21]))
        self.button_list[22].config(
            command=lambda: self.display(self.key_value_list[22]))

    # 定义显示函数
    def display(self, key):
        if key == 'MC':
            self.memory_state.set('')
            self.memory_value = ''
        elif key == 'M+' or key == 'M-':
            if self.output_value.get() != "ERROR":
                self.memory_value = str(
                    eval(self.memory_value + key[-1] + self.output_value.get()))
            self.memory_state.set('M')
        elif key == "MR":
            if self.memory_state.get():
                self.input_value.set(self.memory_value)
        elif key == "=":
            if self.output_value.get() != 'ERROR':
                self.input_value.set(self.output_value.get())
        elif key == "C":
            self.input_value.set('')
        elif key == "⬅":
            self.input_value.set(self.input_value.get()[:-1])
        elif key == '-':
            if self.input_value.get() == '' or self.input_value.get() == '-':
                self.input_value.set(key)
            elif self.input_value.get()[-1] in ["+", "-", "x", "÷"]:
                self.input_value.set(self.input_value.get()[:-1] + key)
            else:
                self.input_value.set(self.input_value.get() + key)
        elif key in ["+", "x", "÷"]:
            if self.input_value.get() == '' or self.input_value.get() == '-':
                self.input_value.set(self.input_value.get())
            elif self.input_value.get()[-1] in ["+", "-", "x", "÷"]:
                self.input_value.set(self.input_value.get()[:-1] + key)
            else:
                self.input_value.set(self.input_value.get() + key)
        else:
            self.input_value.set(self.input_value.get() + key)
        self.output_value.set(self.input_value.get())
        output_value_str = self.output_value.get().replace(
            'x', '*').replace('÷', '/').replace('%', '/100')
        if output_value_str:
            if output_value_str[-1] in ["+", "-", "*", "/"]:
                output_value_str = output_value_str[:-1]
            try:
                output_value = eval(output_value_str)
            except:
                self.output_value.set('ERROR')
            else:
                output_value_str = str(output_value)
                if len(output_value_str) > 25:
                    output_value_str = f"{output_value:e}"
                self.output_value.set(output_value_str)

    # 定义接收键盘输入显示函数
    def key_display(self, event):
        # print(event.keysym)
        if event.keysym == "BackSpace":
            key = "⬅"
        elif event.char == '/':
            key = '÷'
        elif event.char in self.key_value_list:
            key = event.char
        else:
            key = ''
        self.display(key)


# 测试
if __name__ == '__main__':
    root = Tk()  # 创建根窗口
    root.title('简易计算器')
    Application(root)  # 创建实例
    root.mainloop()  # 开启主循环
