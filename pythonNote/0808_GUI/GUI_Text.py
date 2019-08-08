# -*- coding: utf-8 -*

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        # Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
        Frame.__init__(self, master)

        # 布局: pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 输入
        self.userInput = Entry(self)
        self.userInput.pack()

        self.confirmButton = Button(self, text='Hello', command=self.hello)
        self.confirmButton.pack()

    def hello(self):
        # 输入内容
        userInput = self.userInput.get() or 'world'
        # 使用tkMessageBox.showinfo()可以弹出消息对话框
        tkMessageBox.showinfo('Message', 'Input: , %s' % userInput)

app = Application()
# 设置窗口标题:
app.master.title('我是一个title')
# 主消息循环:
app.mainloop()
