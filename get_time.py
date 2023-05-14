import tkinter as tk
from datetime import datetime
from tkinter import font
import os

time = datetime.now().strftime("%Y-%m-%d %H%M")
# 获取当前文件所在目录的绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
# 获取上两级目录的绝对路径
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir)) 
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir)) + f'\数据\串口采集数据\{time}.txt'


timestamps = []  # 用于保存时间戳的列表

def save_timestamp():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    
    timestamps.append(timestamp)  # 将时间戳添加到列表中
    print("时间戳已保存。")

def write_to_file():
    with open( parent_dir, "w") as file:
        for timestamp in timestamps:
            file.write(timestamp + "\n")
    print("时间戳已保存至文件。")

# 创建主窗口
window = tk.Tk()
window.title("保存时间戳")
window.geometry("500x300")

# 创建按钮
button_font = font.Font(size=16)
button_save = tk.Button(window, text="保存时间戳", command=save_timestamp,width=30, height=5,font= button_font)
button_save.pack(padx=20, pady=10)

button_write = tk.Button(window, text="写入文件", command=write_to_file,width=30, height=5,font= button_font)
button_write.pack(padx=20, pady=10)

# 运行主循环
window.mainloop()


