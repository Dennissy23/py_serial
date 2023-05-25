import serial
import time
import datetime
import os
import threading
from BLE_GNSS import read_GNSS_port
                    

time_now = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
current_dir = os.path.abspath(os.path.dirname(__file__))
# 获取上两级目录的绝对路径
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir)) 
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir)) + f'\数据\串口采集数据\RTK_{time_now }.csv'
print('GNSS_begain')



port = 'COM6'
baud_rate = 115200
stop_flag = threading.Event()
read_GNSS_port(port, baud_rate,parent_dir)
    


