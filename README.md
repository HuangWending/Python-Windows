# Python-Windows
Python窗口Hello,HuangWending程序
import tkinter as tk：导入tkinter模块并将其重命名为tk，这是Python的标准图形用户界面（GUI）库。
window = tk.Tk()：创建一个Tk()对象，它表示窗口实例。
window.title("黄文定的窗口")：设置窗口的标题为"黄文定的窗口"。
window.geometry("400x300")：设置窗口的大小为宽度400像素，高度300像素。
label = tk.Label(window, text="Hello, HuangWending!")：创建一个标签对象，它将显示文本"Hello, HuangWending!"。
label.pack()：将标签放置在窗口中心。
window.mainloop()：进入窗口的事件循环，监听并处理与窗口相关的事件，直到窗口被关闭。
