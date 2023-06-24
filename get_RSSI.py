import BLE_GNSS
import threading
import datetime
import csv
import os

time = datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")
# 获取当前文件所在目录的绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
# 获取上两级目录的绝对路径
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir)) 
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir)) + f'\数据\串口采集数据\RSSI_{time}.csv'

mac = [] 
with open('测试信标数据.csv', 'r') as file:
	csv_reader = csv.reader(file)
	# 跳过标题行
	next(csv_reader)
	# 读取每一行的第二列数据并添加到列表中
	for row in csv_reader:
		mac.append(row[1])

stop_flag = threading.Event()
port = "COM4"
baud_rate = 115200
file = parent_dir
print('BLE_Begin')

BLE_GNSS.read_RSSI_port(port, baud_rate,mac,file)
    