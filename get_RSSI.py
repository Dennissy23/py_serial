import BLE
import threading
import datetime
import csv

mac = [] 
with open('信标数据.csv', 'r') as file:
	csv_reader = csv.reader(file)
	# 跳过标题行
	next(csv_reader)
	# 读取每一行的第二列数据并添加到列表中
	for row in csv_reader:
		mac.append(row[1])

stop_flag = threading.Event()
port = "COM10"
baud_rate = 115200
timestamp = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
file = f'dataset\RSSI_{timestamp}.csv'
print('Begin')

BLE.read_serial_data(port, baud_rate,mac,file)
    