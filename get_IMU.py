# -*- coding: utf-8 -*-
from hipnuc_module import *
import datetime
import os

time = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
# 获取当前文件所在目录的绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
# 获取上两级目录的绝对路径
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir)) 
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir)) + f'\数据\串口采集数据\IMU_{time}.csv'

log_file = parent_dir

if __name__ == '__main__':

    m_IMU = hipnuc_module('config.json')
    print("Press Ctrl-C to terminate while statement.")

try: 
    #create csv file
    m_IMU.create_csv(log_file)
    
    while True:
        try:
            data = m_IMU.get_module_data(10)
            
            #write to file as csv format, only work for 0x91, 0x62(IMUSOL), or there will be error
            m_IMU.write2csv(data, log_file)
        
            #time.sleep(0.10)
        except:   
            print("Error")
            m_IMU.close()
            break

except KeyboardInterrupt:
            print("Serial is closed.")
            m_IMU.close()
            pass