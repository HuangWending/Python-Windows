import tkinter as tk

# 创建一个窗口实例
window = tk.Tk()

# 设置窗口的标题
window.title("黄文定的窗口")

# 设置窗口的大小
window.geometry("400x300")

# 创建标签
label = tk.Label(window, text="Hello, HuangWending!")

# 将标签放置在窗口中心
label.pack()

# 进入窗口的事件循环
window.mainloop()
