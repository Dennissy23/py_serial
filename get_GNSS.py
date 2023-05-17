import serial
import time

def read_from_port(serial_port):
    while True:
        if serial_port.in_waiting > 0:
            # 读取一行数据，使用decode()方法将bytes转换为str
            line = serial_port.readline().decode('ascii')
            print(line)


# 创建一个串口实例，端口为COM3，波特率为9600，超时设为1秒
serial_port = serial.Serial("COM6", 115200, timeout=1)
time.sleep(2)  # 等待串口打开

try:
    read_from_port(serial_port)
except KeyboardInterrupt:  # 按Ctrl+C退出
    print("程序被用户终止")
finally:
    # 关闭串口
    serial_port.close()

