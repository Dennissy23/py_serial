import serial
import time
import datetime
import csv
import os
def read_from_port(serial_port,filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        while True:
            if serial_port.in_waiting > 0:
                # 读取一行数据，使用decode()方法将bytes转换为str
                line = serial_port.readline().decode('ascii')
                timestemps = time.time()
                data = line.split(',')
                gnss_data = data[1:3,4:5]
                gnss_data.insert(0, timestemps)
                csv_writer.writerow(gnss_data)
                print(line)

time = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
current_dir = os.path.abspath(os.path.dirname(__file__))
# 获取上两级目录的绝对路径
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir)) 
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir)) + f'\数据\串口采集数据\RTK_{time}.csv'

serial_port = serial.Serial("COM6", 115200, timeout=1)
time.sleep(2)  # 等待串口打开

try:
    read_from_port(serial_port,parent_dir)
except KeyboardInterrupt:  # 按Ctrl+C退出
    print("程序被用户终止")
finally:
    # 关闭串口
    serial_port.close()

